# pages/exportar.py
import streamlit as st
import pandas as pd
from io import BytesIO
from utils import listar_produtos_exportar

def exibir():
    st.title("Exportar Produtos para Excel")

    produtos = listar_produtos_exportar()
    if not produtos:
        st.info("Nenhum produto para exportar.")
        return

    # Criar DataFrame
    df = pd.DataFrame(produtos, columns=["ID", "Nome", "Descrição", "Preço", "ImagemUrl"])
    st.dataframe(df)

    # Criar arquivo Excel em memória
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Produtos")

    buffer.seek(0)

    # Botão de download
    st.download_button(
        label="📥 Baixar Excel",
        data=buffer,
        file_name="produtos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
