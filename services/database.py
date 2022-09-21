import mysql.connector
from os import environ

HOST = environ.get('HOST', 'escreva-o-host-aqui')
PASSWD = environ.get('PASSWD', 'escreva-o-passwd-aqui')
USER = environ.get('USER', 'escreva-o-user-aqui')
DATABASE = environ.get('DATABASE', 'escreva-o-db-name-aqui')

bdConnection = mysql.connector.connect(
    host=f'{HOST}',
    user=f'{USER}',
    password=f'{PASSWD}',
    database=f'{DATABASE}',
)  # Conexão com dados do banco de dados e MySQL

cursor = bdConnection.cursor()  # Cursor para executar conexão
bdConnection.commit()