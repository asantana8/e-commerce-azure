# pages/listar.py
import streamlit as st
from utils import listar_produtos


def exibir():
    st.title("Produtos Cadastrados")

    termo = st.text_input("Buscar por nome")
    produtos = listar_produtos(termo)

    if not produtos:
        st.info("Nenhum produto encontrado.")
        return

    for i in range(0, len(produtos), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(produtos):
                p = produtos[i + j]
                with col:
                    st.image(p[4], width=150)
                    st.subheader(p[1])
                    st.caption(f"R$ {p[3]:.2f}")
                    st.text(p[2])
