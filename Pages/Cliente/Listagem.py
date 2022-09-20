import streamlit as st
import Controller.clienteController as clienteController
import Pages.Cliente.Cadastro as PageCadastro

def Listagem():
    paramId = st.experimental_get_query_params()
    if paramId == {}:  # Se parâmetro de atualização está zerado, listagem normal de clientes.
        st.experimental_set_query_params()
        st.title("Lista de clientes :clipboard:")
        columns = st.columns((1, 2, 1, 2, 1, 1))
        atributes = [':file_folder: ID', ':page_facing_up: Nome', ':calendar: Idade', ':construction_worker: Profissão', ':x: Excluir', ':arrows_clockwise: Alterar']
        for coluna, atribute_name in zip(columns, atributes):
            coluna.write(atribute_name)

        for x, item in enumerate(clienteController.SelecionarClientes()):
            coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 = st.columns((1, 2, 1, 2, 1, 1))
            coluna1.write((str(item.id)))
            coluna2.write(item.nome)
            coluna3.write(str(item.idade))
            coluna4.write(item.profissao)
            buttonDelete = coluna5.empty()
            delClick = buttonDelete.button('Excluir', 'botãoExcluir' + str(item.id))
            # str(itemid+1) para concatenar com a string de key 'botaoExcluir' e evitar redundancia.
            buttonChange = coluna6.empty()
            changeClick = buttonChange.button('Alterar', 'botãoAlterar' + str(item.id))
            # str(itemid+1) para concatenar com a string de key 'botaoAlterar' e evitar redundancia.

            if delClick:
                clienteController.Excluir(item.id)
                st.experimental_rerun()  # Reload da page para o cliente "sumir" da listagem
            if changeClick:
                st.experimental_set_query_params(
                    id=[item.id]
                ) # Setando o parâmetro de ID na URL para dar GET na página de cadastro
                st.experimental_rerun()  # Reload de garantia
    else:
        PageCadastro.Cadastrar()  # Cadastro no modo 'Atualizar Cad.' pois parâmetro de id não está zerado.
        clickBack = st.button('Voltar')
        if clickBack:
            st.experimental_set_query_params()  # Zerando parâmetro para liberar da tela de atualização
            st.experimental_rerun()  # Reload
