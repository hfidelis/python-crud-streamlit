from services import database as db
from Controller.models.Cliente import Cliente as cliente

def Incluir(cliente):
    db.cursor.execute(f'INSERT INTO clientes (nomeCliente, idadeCliente, profissaoCliente)'
                      f'VALUES ("{cliente.nome}", {cliente.idade}, "{cliente.profissao}")')
    db.bdConnection.commit()

def SelecionarClientes():
    selectCommand = f'SELECT * FROM clientes'
    db.cursor.execute(selectCommand)
    clienteList = []
    for row in db.cursor.fetchall():
        clienteList.append(cliente(row[0], row[1], row[2], row[3]))

    return clienteList

def Excluir(id):
    deleteCommand = f'DELETE FROM clientes WHERE idClientes = {id}'
    db.cursor.execute(deleteCommand)
    db.bdConnection.commit()

def Alterar(cliente):
    updateCommand = f'UPDATE clientes SET nomeCliente = "{cliente.nome}", idadeCliente = {cliente.idade},' \
                    f' profissaoCliente = "{cliente.profissao}"' \
                    f'WHERE idClientes = {cliente.id}'
    db.cursor.execute(updateCommand)
    db.bdConnection.commit()

def SelecionarID(id):
    selectId = f'SELECT * FROM clientes WHERE idClientes = {id}'
    db.cursor.execute(selectId)
    idList = []
    for row in db.cursor.fetchall():
        idList.append(cliente(row[0], row[1], row[2], row[3]))

    return idList[0]  #Retornando a lista apenas com o valor necessário, que é o ID, da coluna 0 na database
