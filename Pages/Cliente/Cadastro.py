import streamlit as st
import Controller.models.Cliente as Cliente  # import da classe Cliente
import Controller.clienteController as ClienteController  # Funções de cliente

def Cadastrar():
    idAlterar = st.experimental_get_query_params()
    st.experimental_set_query_params()
    clienteRecover = None
    if idAlterar.get("id") is not None:
        # Se o parâmetro não estiver zerado, no caso quando o usuário já selecionou para alterar
        idAlterar = idAlterar.get("id")[0]  # idAlterar = posição 0 do array ID
        clienteRecover = ClienteController.SelecionarID(idAlterar)  # clienteRecover = cliente selecionado para alterar,
        # a partir da função Select by ID
        st.experimental_set_query_params(
            id=[clienteRecover.id]
        )  # Definindo o parâmetro de alteração para o cliente a ser alterado
        st.title('Alterar cadastro :pencil2:')
    else:
        st.title('Cadastrar :white_check_mark:')

    with st.form(key='include_cliente'):
        workList = ['Desenvolvedor Web', 'Designer', 'Engenheiro', 'DevOps', 'Estudante', 'Analista']
        if clienteRecover is None:
            input_name = st.text_input(label='Insira o nome do cliente:', placeholder='Nome')
            input_age = st.number_input(label='Insira a idade do cliente:', format='%i', step=1,
                                        min_value=18, max_value=120)
            input_work = st.selectbox('Selecione a profissão do cliente:', options=workList)
        else:
            input_name = st.text_input(label='Insira o nome do cliente:', value=clienteRecover.nome)
            input_age = st.number_input(label='Insira a idade do cliente:',
                                        format='%i', step=1, min_value=18, max_value=120, value=clienteRecover.idade)
            input_work = st.selectbox('Selecione a profissão do cliente:',
                                      options=workList, index=workList.index(clienteRecover.profissao))
        input_button_submit = st.form_submit_button("Enviar")
        # inputs com valores do cliente a ser alterado p/ update visual

    if input_button_submit:
        if clienteRecover is None:
            ClienteController.Incluir(Cliente.Cliente(0, input_name, input_age, input_work))
            # Função de incluir cliente na database com cursor e commit
            st.success("Sucesso! Cliente cadastrado!")
        else:
            st.experimental_set_query_params()
            ClienteController.Alterar(Cliente.Cliente(clienteRecover.id, input_name, input_age,
                                                      input_work))
            # Função de alterar cliente na database com cursor e commit
            # valor de id é o ID do cliente a ser alterado, (clienteRecover.id), fazendo update na database
            st.success("Sucesso! Cliente alterado!")
