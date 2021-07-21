
                                                  ###EXTRAI DADOS DO GINLONG 10.80.0.12###

import socket, binascii, time, codecs
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
from collections import defaultdict
import numpy as np            #biblioteca para trabalhar com int32 ex.: foo = np.int32(3)
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


HOST = '0.0.0.0'              # Endereco IP do Servidor
PORT = 9999                   # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)                 # Coloca porta em escuta

ipBusModbus = '10.80.0.80'    # ip do servidor modbus
portaServerModbus = 502       # porta do servidor modbus

dataStore = defaultdict(np.int32) #criando um vetor do tipo int32 (32 bits)
primeiroEnderecoMB = 50           #primeiro endereço do registrador modbus

header1 = binascii.unhexlify ('685951b0')               
header = binascii.hexlify(header1) 			


                                                        
inverter_now = 59 					# posição inicial do vetor de dados da geração instantânea
inverter_day = 69 					# posição inicial do vetor de dados da geração diária
inverter_tot = 73 					# posição inicial do vetor de dados da geração total
inverter_mth = 87					# posição inicial do vetor de dados da geração mensal 


#cria instância do cliente modbus
client = ModbusClient(ipBusModbus, portaServerModbus)

def conectServidorModbus():
    '''função para conectar no servidor modbus'''
    try:
        client.connect()
    except Exception as e:
        print(str(e), "--> Exception ao tentar conectar no barramento modbus")


#tentando conectar no servidor modbus
conectServidorModbus()

                                    ###FUNCAO PARA CAPTURAR DDOS DO INVERSOR GINLONG###

def capturarDadosInversor():
    con, cliente = tcp.accept()
    msg = con.recv(1024)            #Espera o dado chegar(o dado vem em forma de vetor)
    hexdata = binascii.hexlify(msg) #Transformando dados de decimal para hexadecimal
    
                                    ###TRANSFORMANDO DADOS DE HEXADECIMAL PARA DECIMAL###
    
    dataStore[0] = int(hexdata[inverter_now*2:inverter_now*2+4],16)    		        # generating power in watts
    dataStore[1] = int(hexdata[inverter_day*2:inverter_day*2+4],16)	                # running total kwh for day
    dataStore[2] = int(hexdata[inverter_mth*2:inverter_mth*2+4],16)		        # running total kwh for month
    dataStore[3] = int(int(hexdata[inverter_tot*2:inverter_tot*2+4],16)/10)	        # running total kwh from installation
    print(dataStore[0], dataStore[1], dataStore[2], dataStore[3])


def int32toint16( index ):
    '''função para converter int32 em int16'''
    dataHigh = dataStore[index] >> 16
    dataLow = dataStore[index] & 0xFFFF
    return(dataHigh, dataLow)

                                                ###LOOP INFINITO###

while True:

    capturarDadosInversor()
    #tenta conectar no servidor modbus se não conectado
    if not(client.is_socket_open()):
        conectServidorModbus()
    #armazena os valores no barramento apenas se conectado no servidor
    if client.is_socket_open():
        for index in range(4):
        #log.debug("Write to multiple holding registers")
            dataHigh, dataLow = int32toint16(index)
            rq = client.write_registers(primeiroEnderecoMB + ( index * 2 ), dataHigh, unit=1) #escrevendo dado no servidor modbus
            rq = client.write_registers(primeiroEnderecoMB + (index * 2 ) + 1, dataLow, unit=1) #escrevendo dado no servidor modbus
            


    

con.close()
