# API RESTful com Flask

## Descrição
Esta é uma API RESTful simples desenvolvida com Flask para gerenciar uma lista de filmes. A API permite realizar operações CRUD (Create, Read, Update, Delete) em um "banco de dados" em memória, simulando o funcionamento de sistemas reais de gerenciamento de informações.

---

## Funcionalidades
1. **Adicionar Filmes** (POST `/movies`): Permite adicionar novos filmes com informações como título, diretor e ano.
2. **Listar Filmes** (GET `/movies`): Retorna a lista de todos os filmes cadastrados.
3. **Atualizar Filmes** (PUT `/movies/<id>`): Atualiza as informações de um filme com base no ID.
4. **Deletar Filmes** (DELETE `/movies/<id>`): Remove um filme da lista com base no ID.

---

## Tecnologias Utilizadas

- **Python 3.10 ou superior**
- **Flask 3.1.0**: Framework para criação de APIs.

---

## Como Configurar o Projeto

### 1️⃣ Requisitos

Certifique-se de ter o Python instalado em seu sistema.
Para verificar, execute:
```bash
python --version
```

### 2️⃣ Criar o Ambiente Virtual
1. **Navegue até a pasta do projeto:**
   ```bash
   cd /caminho/para/api_project
   ```
2. **Crie o ambiente virtual:**
   ```bash
   python -m venv venv
   ```
3. **Ative o ambiente virtual:**
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

### 3️⃣ Instale as Dependências

Com o ambiente virtual ativo, instale o Flask:
```bash
pip install flask
```

Salve as dependências no arquivo `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## Como Rodar o Projeto

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o arquivo principal `app.py`:
   ```bash
   python app.py
   ```
3. Acesse o endpoint inicial no navegador ou com ferramentas como Postman:
   ```
   http://127.0.0.1:5000/movies
   ```

---

## Endpoints da API

### **1. Adicionar um Filme**
- **Método:** POST
- **URL:** `/movies`
- **Body (JSON):**
  ```json
  {
    "title": "O Poderoso Chefão",
    "director": "Francis Ford Coppola",
    "year": 1972
  }
  ```
- **Resposta:**
  ```json
  {
    "message": "Filme adicionado com sucesso!",
    "movie": {
      "id": 1,
      "title": "O Poderoso Chefão",
      "director": "Francis Ford Coppola",
      "year": 1972
    }
  }
  ```

### **2. Listar Todos os Filmes**
- **Método:** GET
- **URL:** `/movies`
- **Resposta:**
  ```json
  [
    {
      "id": 1,
      "title": "O Poderoso Chefão",
      "director": "Francis Ford Coppola",
      "year": 1972
    }
  ]
  ```

### **3. Atualizar um Filme**
- **Método:** PUT
- **URL:** `/movies/<id>`
- **Body (JSON):**
  ```json
  {
    "title": "O Poderoso Chefão: Parte II"
  }
  ```
- **Resposta:**
  ```json
  {
    "message": "Filme atualizado com sucesso!",
    "movie": {
      "id": 1,
      "title": "O Poderoso Chefão: Parte II",
      "director": "Francis Ford Coppola",
      "year": 1972
    }
  }
  ```

### **4. Deletar um Filme**
- **Método:** DELETE
- **URL:** `/movies/<id>`
- **Resposta:**
  ```json
  {
    "message": "Filme removido com sucesso!"
  }
  ```

---

## Como Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, desative o ambiente virtual para liberar o terminal:

```bash
deactivate
```

---

## Melhorias Futuras
1. Implementar validação de dados.
2. Persistir os dados em um banco de dados como SQLite.
3. Adicionar autenticação e autorização para proteger os endpoints.

---

## Licença

Projeto de uso livre para aprendizado e estudos.

##Autor
Criado por MPSPG
