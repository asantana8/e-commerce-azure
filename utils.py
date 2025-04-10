# utils.py
import os
import pyodbc
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

# Azure Blob
blobConnectionString = os.getenv("BLOB_CONNECTION_STRING").strip('"')
blobContainerName = os.getenv("BLOB_CONTAINER_NAME").strip('"')
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME").strip('"')

blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
container_client = blob_service_client.get_container_client(blobContainerName)

def get_blob_client(filename):
    return container_client.get_blob_client(filename)

# 🔁 Função para gerar conexão nova
def get_conn():
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 18 for SQL Server}};'
        f'SERVER={os.getenv("SQL_SERVER").strip("\"")};'
        f'DATABASE={os.getenv("SQL_DATABASE").strip("\"")};'
        f'UID={os.getenv("SQL_USER").strip("\"")};'
        f'PWD={os.getenv("SQL_PASSWORD").strip("\"")};'
        f'TrustServerCertificate=yes;'
    )
    conn.autocommit = True
    return conn

# 🧩 CRUD isolado por conexão
def insert_produto(nome, desc, preco, url):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Produtos (Nome, Descricao, Preco, ImagemUrl)
                VALUES (?, ?, ?, ?)
            """, (nome, desc, preco, url))
        

def listar_produtos(filtro_nome=""):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            if filtro_nome:
                cursor.execute("SELECT * FROM Produtos WHERE Nome LIKE ?", (f"%{filtro_nome}%",))
            else:
                cursor.execute("SELECT * FROM Produtos")
            return cursor.fetchall()   
        

def atualizar_produto(id, nome, desc, preco):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE Produtos SET Nome=?, Descricao=?, Preco=? WHERE Id=?
            """, (nome, desc, preco, id))
        

def excluir_produto(id):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Produtos WHERE Id=?", (id,))


def listar_produtos_exportar():
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Id, Nome, Descricao, Preco, ImagemUrl FROM Produtos")
            rows = cursor.fetchall()
            return [tuple(r) for r in rows]  # Garante que cada linha seja uma tupla simples


