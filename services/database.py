import mysql.connector

bdConnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Heit@r3270xxx',
    database='teste',
)  # Conexão com dados do banco de dados e MySQL

cursor = bdConnection.cursor()  # Cursor para executar conexão
bdConnection.commit()
