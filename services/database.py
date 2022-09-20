import mysql.connector

bdConnection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Heit@r3270xxx',
    database='teste',
)  # Conexão com dados do banco de dados e MySQL

cursor = bdConnection.cursor()  # Cursor para executar conexão
bdConnection.commit()
