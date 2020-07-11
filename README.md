# script-zipper-helper
Repositório com um script simples em python para automatizar os pacotes de ZIP utilizados para fazer deploy em servidores SQL.


#How to use 
No arquivo settings.json, altere os nomes dos servidores de banco de dados  e o database,


```json
{
  "filename": "Roteiro_Execucao_BD.csv",
  "encoding": "cp1252",
  "servers": [
    "SERVER1",
    "SERVER2",
    "SERVER3",
    "SERVER4"
  ],
  "database": "DATABASE_NAME",
  "scriptsPath": "../scripts"
}
```

Adicione os scripts dentro da pasta **scripts**

![Scripts folder](https://imgur.com/3NGSg8i.png)

 Acesse a pasta e execute o script 

```sh
$ python python/script.py
```

##### Arquivos gerados

Cada zip file é um servidor que foi cadastrado no settings.json

![Output](https://imgur.com/yZn3NqG.png)

Arquivos dentro do zip 

![Output](https://imgur.com/PtJFXp4.png)

Roteiro gerado

![Output](https://imgur.com/4a5CfWz.png)

