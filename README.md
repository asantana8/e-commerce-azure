**E-Commerce na Cloud com Streamlit + Azure Blob + SQL Server**:

---

```markdown
# 🛒 E-Commerce na Cloud

Aplicação web simples de cadastro e listagem de produtos utilizando **Streamlit**, **Azure Blob Storage** e **SQL Server na Azure**.

## 🚀 Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/)
- [Azure Blob Storage](https://azure.microsoft.com/pt-br/products/storage/blobs/)
- [SQL Server (Azure)](https://azure.microsoft.com/pt-br/products/azure-sql/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [pyodbc](https://pypi.org/project/pyodbc/)

---

## ⚙️ Funcionalidades

- Cadastro de produtos com:
  - Nome
  - Descrição
  - Preço
  - Imagem (salva no Azure Blob)
- Armazenamento dos dados no SQL Server
- Exibição dos produtos cadastrados com imagem e descrição

---

## 🧪 Requisitos

- Python 3.10 ou superior
- [ODBC Driver 18 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server)
- Conta e container no **Azure Blob Storage**
- Banco de dados no **Azure SQL Server**

---

## 🛠️ Instalação

```bash
# Clone o projeto
git clone https://github.com/seuusuario/ecommerce-na-cloud.git
cd ecommerce-na-cloud

# Crie um ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

---

## 🔐 Configuração do .env

Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais:

```env
BLOB_CONNECTION_STRING="sua_connection_string"
BLOB_CONTAINER_NAME="nome_do_container"
BLOB_ACCOUNT_NAME="nome_da_conta_blob"

SQL_SERVER="seu-servidor.database.windows.net"
SQL_DATABASE="nome_do_banco"
SQL_USER="usuario"
SQL_PASSWORD="senha"
```

---

## 🧮 Estrutura da Tabela no Banco

```sql
CREATE TABLE Produtos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nome NVARCHAR(100),
    Descricao NVARCHAR(MAX),
    Preco FLOAT,
    ImagemUrl NVARCHAR(MAX)
);
```

---

## ▶️ Executando a aplicação

Com o ambiente ativado e `.env` configurado:

```bash
streamlit run main.py
```

Acesse no navegador: [http://localhost:8501](http://localhost:8501)

---

## 📸 Demonstração

*(Adicione aqui prints ou um gif da aplicação rodando)*

---

## 🧑‍💻 Autor

**Adriano Santana**  
Projeto feito com fins de aprendizado em cloud computing, Azure e aplicações web com Python.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

---
