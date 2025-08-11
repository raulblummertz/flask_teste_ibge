# API para indicadores do IBGE

## Sobre o Projeto

Este projeto foi desenvolvido para ser uma aplicação que verifica indicadores do IBGE através de requisições para API e insere em um banco relacional para futuras consultas, operando da seguinte maneira:

1.  É definido a lista de países e indicadores a serem consultados na aplicação;
2.  A aplicação recebe os dados em formato JSON e normaliza para estrutura de DataFrame;
3.  Após normalizar, insere os dados transformados tabelas distintas para cada indicador.

## Funcionalidades Principais

-   **Extração de dados:** Extrai, via requisições, os dados de cada país e indicador.
-   **Transformação dos dados:** Transforma os dados recebidos em formato JSON para estrutura tabular, mantendo somente os dados relevantes.
-   **Inserção no bando de dados:** Insere os dados transformados em tabelas distintas, em um banco de dados PostgreSQL

## Tecnologias Utilizadas

-   **Linguagem:** Python 3.13.5
-   **Framework:** Flask
-   **Banco de Dados:** PostgreSQL
-   **ORM:** SQLAlchemy
-   **Transformação de dados:** Pandas

## Estrutura do Projeto

A estrutura de pastas e arquivos principais do projeto é a seguinte:
```
├── flask-teste-IBGE/
│   ├── pycache/
│   ├── app.py              # Arquivo contendo toda a lógica da aplicação
│   ├── requirements.txt    # Lista de dependências do projeto
│   ├── Dockerfile          # Funções para gerar embeddings
│   ├── docker-compose.yml  # Arquivo principal da API com FastAPI
```
## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Pré-requisitos

-   Python 3.13 ou superior instalado.
-   Git instalado.
-   Docker instalado.

### 2. Clonar o Repositório

```
git clone https://github.com/raulblummertz/flask-teste-ibge.git cd <NOME_DA_PASTA_DO_PROJETO>
```
### 3. Configurar Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e adicione as variáveis de ambiente necessárias:

```
DB_URL = diretorio_do_seu_banco
```
### 4. Configurar a imagem do Dockerfile

Altere o parâmetro **image** dentro do service **flask_app** para o seu usuário do DockerHub
```
services:
    flask_app:
      container_name: flask_app
      image: seu_user/flask_app:1.0.0
      ...
```

## Como Usar
Para colocar o sistema em funcionamento, você precisa executar os comandos na seguinte ordem.

### 1. Criar a imagem do banco de dados no seu container Docker
Primeiro, execute o comando no terminal para criar a imagem do seu banco de dados Postgres no container.

```docker compose up -d flask_db```

### 2. Buildar a imagem da aplicação
Ainda no terminal, crie a imagem contendo a aplicação que será executada.

```docker compose build```


### 3. Rode a aplicação no seu container
Continuando no terminal, execute o seguinte comando para subir a aplicação
```docker compose up flask_app```

### 4. Teste a rota da API
Acesse a rota da API definida na aplicação para que o seu banco de dados seja populado.

```http://localhost:5000/paises/```

Após esses passos, você pode usar a ferramenta de sua preferência para verificar as tabelas criadas no banco de dados.
