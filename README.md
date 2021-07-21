# i2s-gerador-eolico-ginlong
extrator de dados do gerador eólico da marca Ginlong

# **EXTRATOR DE DADOS DO INVERSOR GINLONG**
<br>
___
<br>

#Executar um código para cada inversor alterando as constantes

### Endereço IP do servidor Ginlong
```
ipG1 = '10.80.0.27'
ipG2 = '10.80.0.12'
ipG3 = '10.80.0.25'
```
### Endereço IP do servidor modbus
```
ipBusModbus = '10.80.0.80'
```
### Porta TCP do servidor modbus
```
portaServerModbus = 502
```
### Primeiro endereço do barramento MB utilizado pelo inversor. 
```
primeiroEnderecoMB = 50(G1)
primeiroEnderecoMB = 60(G2)
primeiroEnderecoMB = 70(G3)
```

## ENDEREÇAMENTO MODBUS
```
valores em Wh
INVERSOR G1 - JIT211
50 = PAC parte alta
51 = PAC parte baixa
52 = DAY_ENERGY parte alta
53 = DAY_ENERGY parte baixa
54 = MONTH_ENERGY parte alta
55 = MONTH_ENERGY parte baixa
56 = TOTAL_ENERGY parte alta
57 = TOTAL_ENERGY parte baixa
58 = YEAR_ENERGY parte alta
59 = YEAR_ENERGY parte baixa

INVERSOR G2 - JIT212
60 = PAC parte alta
61 = PAC parte baixa
62 = DAY_ENERGY parte alta
63 = DAY_ENERGY parte baixa
64 = MONTH_ENERGY parte alta
65 = MONTH_ENERGY parte baixa
66 = TOTAL_ENERGY parte alta
67 = TOTAL_ENERGY parte baixa
68 = YEAR_ENERGY parte alta
69 = YEAR_ENERGY parte baixa

INVERSOR G3 = GIT213
70 = PAC parte alta
71 = PAC parte baixa
72 = DAY_ENERGY parte alta
73 = DAY_ENERGY parte baixa
74 = MONTH_ENERGY parte alta
75 = MONTH_ENERGY parte baixa
76 = TOTAL_ENERGY parte alta
77 = TOTAL_ENERGY parte baixa
78 = YEAR_ENERGY parte alta
79 = YEAR_ENERGY parte baixa



```


<br>
___
<br>
# **Usando Git**

### Clonando repositório
```
git clone http://gitlab.nc2.iff.edu.br/i2s/extratorGinlong.git
```

### Navegue até a pasta
```
cd ExtratorG1
cd ExtratorG2
```

### Iniciando git
```
git init
```

### Verificando status
```
git status
```

### Fazendo git reconhecer modificações em arquivo
```
git add nome_do_arquivo
```
*Obs: Você pode fazer com que o git registre todos os arquivos usando os seguintes termos no lugar do nome do arquivo: ``` * ``` ou ``` . ``` ou ``` --all ``` .*

### Realizar commit
```
git commit -m "Descrição da minha modificação"
```
*Obs: O commit guarda apenas as modificações registradas pelo ``` git add ``` .*

### ENVIAR MODIFICAÇÕES PARA O SERVIDOR GIT
```
git push origin master
```
*Caso ocorra erro no push, tente usar o comando ``` git remote add origin http://gitlab.nc2.iff.edu.br/i2s/extratorGinlong.git ``` antes.*

*Também podem ocorrer erros devido atualizações no servidor que não foram replicadas para a sua máquina. Nesse caso use o comando ``` git pull ```, que vai atualizar seu repositório local com os dados do repositório remoto.*
<br><br>
___
<br>
*Texto padrão do README.md*

### Git global setup
```
git config --global user.name "William Vianna"
git config --global user.email "wvianna@iff.edu.br"
```
### Create a new repository

` git clone http://gitlab.nc2.iff.edu.br/i2s/extratorGinlong.git `

` cd ExtratorG1 `

` touch README.md `

` git add README.md `

` git commit -m "add README" `

` git push -u origin master `


### Existing folder or Git repository

` cd existing_folder `

` git init `

` git remote add origin http://gitlab.nc2.iff.edu.br/i2s/extratorFronius.git `

` git add . `

` git commit `

` git push -u origin master `

