# pages/cadastro.py
import streamlit as st
import uuid
from utils import get_blob_client, insert_produto, blobAccountName, blobContainerName

def exibir():
    st.title("Cadastrar Produto")

    nome = st.text_input("Nome do Produto")
    descricao = st.text_area("Descrição")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    imagem = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

    if st.button("Salvar"):
        if not all([nome, descricao, preco, imagem]):
            st.warning("Preencha todos os campos!")
            return

        try:
            # Gerar nome único para a imagem            
            imagem_nome = f"{uuid.uuid4()}.{imagem.type.split('/')[-1]}"

            # Upload da imagem
            blob_client = get_blob_client(imagem_nome)
            blob_client.upload_blob(imagem, overwrite=True)

            # URL da imagem
            url_imagem = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{imagem_nome}"
            
            # Inserção no banco
            insert_produto(nome, descricao, preco, url_imagem)

            st.success("Produto cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar produto: {str(e)}")
