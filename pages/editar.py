# pages/editar.py
import streamlit as st
from utils import listar_produtos, atualizar_produto, excluir_produto

def exibir():
    st.title("Editar ou Excluir Produtos")

    produtos = listar_produtos()
    if not produtos:
        st.info("Nenhum produto encontrado.")
        return

    # Lista com nomes formatados
    opcoes = [f"{p[0]} - {p[1]}" for p in produtos]
    escolha = st.selectbox("Selecione um produto", opcoes)

    # Seleciona o produto correspondente
    index = opcoes.index(escolha)
    produto = produtos[index]

    novo_nome = st.text_input("Nome", value=produto[1])
    nova_desc = st.text_area("Descrição", value=produto[2])
    novo_preco = st.number_input("Preço", value=float(produto[3]), format="%.2f")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Atualizar"):
            atualizar_produto(produto[0], novo_nome, nova_desc, novo_preco)
            st.success("Produto atualizado com sucesso!")

    with col2:
        if st.checkbox("Desejo excluir este produto"):
            if st.button("Excluir"):
                excluir_produto(produto[0])
                st.warning("Produto excluído!")
                st.rerun()


