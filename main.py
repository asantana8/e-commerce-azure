# main.py
import streamlit as st
from pages import cadastro, listar, editar, exportar

st.set_page_config(page_title="E-Commerce na Cloud", layout="wide")

st.sidebar.title("Menu")
opcao = st.sidebar.radio("Escolha uma opção:", [
    "Cadastrar Produto",
    "Listar Produtos",
    "Editar/Excluir Produtos",
    "Exportar para Excel"
])

if opcao == "Cadastrar Produto":
    cadastro.exibir()
elif opcao == "Listar Produtos":
    listar.exibir()
elif opcao == "Editar/Excluir Produtos":
    editar.exibir()
elif opcao == "Exportar para Excel":
    exportar.exibir()
