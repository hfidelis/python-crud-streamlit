# 🐍 Python simple CRUD Streamlit Application

## English (en-US) 🇺🇸

This project presents a simple CRUD (Create, Read, Update, Delete) application built with Python and Streamlit, designed for managing user information. It leverages a PostgreSQL database for data persistence and Docker for easy deployment.

### Tech Stack 🔧

*   **Python 3.10+**: The core programming language.
*   **Streamlit**: For building interactive web applications with Python.
*   **SQLAlchemy**: An SQL toolkit and Object-Relational Mapper (ORM) for Python.
*   **Alembic**: A database migration tool for SQLAlchemy.
*   **Pydantic**: Data validation and settings management using Python type hints.
*   **PostgreSQL**: A powerful, open-source relational database.
*   **Poetry**: A dependency management and packaging tool for Python.
*   **Docker & Docker Compose**: For containerization and orchestrating multi-container Docker applications.

### Getting Started

You can run this project using Docker Compose or by setting it up locally.

#### Using Docker Compose 🐳

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/python-crud-streamlit.git
    cd python-crud-streamlit
    ```
2.  **Configure Environment Variables:**
    The `docker-compose.yml` file contains environment variables for the PostgreSQL database (e.g., `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`) and the application's `DATABASE_URL`. You can modify these directly in the `docker-compose.yml` file to suit your needs.
    **Important:** If you change the database connection string in `docker-compose.yml`, you **must also update the `sqlalchemy.url` in `alembic.ini`** to match your new database configuration. This ensures Alembic can connect to the correct database for migrations.
3.  **Build and Run:**
    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker images, start the PostgreSQL database, and launch the Streamlit application.
4.  **Access the Application:**
    Once the containers are up and running, open your web browser and navigate to `http://localhost:8501`.

#### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/python-crud-streamlit.git
    cd python-crud-streamlit
    ```
2.  **Install Poetry (if you don't have it):**
    ```bash
    pip install poetry
    ```
3.  **Install Dependencies:**
    ```bash
    poetry install
    ```
4.  **Set up PostgreSQL:**
    Ensure you have a PostgreSQL database running and accessible. Create a database for the application.
5.  **Configure Environment Variables:**
    Create a `.env` file in the project root or set environment variables directly for your database connection. For example:
    ```
    DATABASE_URL="postgresql://user:password@localhost:5432/your_database_name"
    ```
    **Important:** Ensure the `sqlalchemy.url` in `alembic.ini` matches your local database connection string.
6.  **Run Database Migrations:**
    ```bash
    poetry run alembic upgrade head
    ```
7.  **Run the Streamlit Application:**
    ```bash
    poetry run streamlit run src/main.py
    ```
8.  **Access the Application:**
    Open your web browser and navigate to the address provided by Streamlit (usually `http://localhost:8501`).

---

## Português (pt-BR) 🇧🇷

Este projeto apresenta uma aplicação CRUD (Criar, Ler, Atualizar, Excluir) simples, desenvolvida com Python e Streamlit, projetada para gerenciar informações de usuários. Ele utiliza um banco de dados PostgreSQL para persistência de dados e Docker para facilitar a implantação.

### Tecnologias 🔧

*   **Python 3.10+**: A linguagem de programação principal.
*   **Streamlit**: Para construir aplicações web interativas com Python.
*   **SQLAlchemy**: Um kit de ferramentas SQL e Mapeador Objeto-Relacional (ORM) para Python.
*   **Alembic**: Uma ferramenta de migração de banco de dados para SQLAlchemy.
*   **Pydantic**: Validação de dados e gerenciamento de configurações usando type hints do Python.
*   **PostgreSQL**: Um banco de dados relacional poderoso e de código aberto.
*   **Poetry**: Uma ferramenta de gerenciamento de dependências e empacotamento para Python.
*   **Docker & Docker Compose**: Para conteinerização e orquestração de aplicações Docker multi-container.

### Primeiros Passos

Você pode executar este projeto usando Docker Compose ou configurando-o localmente.

#### Usando Docker Compose 🐳

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/your-repo/python-crud-streamlit.git
    cd python-crud-streamlit
    ```
2.  **Configurar Variáveis de Ambiente:**
    O arquivo `docker-compose.yml` contém variáveis de ambiente para o banco de dados PostgreSQL (por exemplo, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`) e a `DATABASE_URL` da aplicação. Você pode modificá-las diretamente no arquivo `docker-compose.yml` para atender às suas necessidades.
    **Importante:** Se você alterar a string de conexão do banco de dados em `docker-compose.yml`, você **também deve atualizar o `sqlalchemy.url` em `alembic.ini`** para corresponder à sua nova configuração de banco de dados. Isso garante que o Alembic possa se conectar ao banco de dados correto para as migrações.
3.  **Construir e Executar:**
    ```bash
    docker-compose up --build -d
    ```
    Este comando irá construir as imagens Docker, iniciar o banco de dados PostgreSQL e lançar a aplicação Streamlit.
4.  **Acessar a Aplicação:**
    Assim que os contêineres estiverem em execução, abra seu navegador e navegue para `http://localhost:8501`.

#### Executando Localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/your-repo/python-crud-streamlit.git
    cd python-crud-streamlit
    ```
2.  **Instalar Poetry (se você não tiver):**
    ```bash
    pip install poetry
    ```
3.  **Instalar Dependências:**
    ```bash
    poetry install
    ```
4.  **Configurar PostgreSQL:**
    Certifique-se de ter um banco de dados PostgreSQL em execução e acessível. Crie um banco de dados para a aplicação.
5.  **Configurar Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto ou defina as variáveis de ambiente diretamente para a conexão do seu banco de dados. Por exemplo:
    ```
    DATABASE_URL="postgresql://user:password@localhost:5432/nome_do_seu_banco_de_dados"
    ```
    **Importante:** Certifique-se de que o `sqlalchemy.url` em `alembic.ini` corresponda à sua string de conexão do banco de dados local.
6.  **Executar Migrações do Banco de Dados:**
    ```bash
    poetry run alembic upgrade head
    ```
7.  **Executar a Aplicação Streamlit:**
    ```bash
    poetry run streamlit run src/main.py
    ```
8.  **Acessar a Aplicação:**
    Abra seu navegador e navegue para o endereço fornecido pelo Streamlit (default `http://localhost:8501`).

### Screenshots

#### List
![List Clients](docs/list.png)

#### Create
![Create Client](docs/create.png)

#### Edit
![Edit Client](docs/edit.png)

#### Delete
![Delete Client](docs/delete.png)
