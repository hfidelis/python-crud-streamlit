import streamlit as st
import Pages.Cliente.Cadastro as PageCadastro  # Função de cadastrar cliente, com todas as inputs e labels
import Pages.Cliente.Listagem as PageListar  # Função de listar e alterar clientes

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Sistema de clientes :busts_in_silhouette:')  # Título da page
st.sidebar.title(':page_facing_up: Menu')  # Sidebar
sidebarOptions = st.sidebar.selectbox('Cliente', ['Cadastro', 'Consultar/Alterar'])  # Opções da sidebar - Menu

if sidebarOptions == 'Cadastro':
    st.experimental_set_query_params()  # Zerando o set de parâmetro ID para rodar o cadastro sem o modo "Atualizar"
    PageCadastro.Cadastrar()

if sidebarOptions == 'Consultar/Alterar':
    PageListar.Listagem()
