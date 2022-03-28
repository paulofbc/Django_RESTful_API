# API RESTful com Django e SQLite
O código consiste em uma API RESTful em Django com as operações básicas (CRUD) no banco de dados.

## Para rodar o projeto

Primeiro, baixe as dependências do python através do requirements.txt:
``` sh
$ pip install -r requirements.txt
```

Depois rode a API:
``` sh
$ python manage.py runserver
```
Agora o projeto já está rodando e, por padrão, começara em: http://127.0.0.1:8000/

## Testes
No repositório se encontra um arquivo de collection do Postman para testes.
Nesses testes, todas as frentes do CRUD são exploradas. Basta importar essa collection no Postman e executar os requests com o projeto já rodando.
