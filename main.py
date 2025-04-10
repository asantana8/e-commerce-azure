# main.py
import streamlit as st
from pages import cadastro, listar, editar, exportar

# 1️⃣ Deve ser o PRIMEIRO comando Streamlit
st.set_page_config(page_title="E-Commerce", layout="wide", initial_sidebar_state="auto")

# Oculta o menu lateral automático do Streamlit
hide_menu_style = """
        <style>
        [data-testid="stSidebarNav"] {display: none;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Importa suas funcionalidades
import pages.cadastro as cadastro
import pages.listar as listar
import pages.editar as editar
import pages.exportar as exportar

# Menu principal
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Escolha uma opção:", [
    "Cadastrar Produtos",
    "Listar Produtos",
    "Editar/Excluir Produtos",
    "Exportar para Excel"
])

# Roteia para cada função
if opcao == "Cadastrar Produtos":
    cadastro.exibir()
elif opcao == "Listar Produtos":
    listar.exibir()
elif opcao == "Editar/Excluir Produtos":
    editar.exibir()
elif opcao == "Exportar para Excel":
    exportar.exibir()
