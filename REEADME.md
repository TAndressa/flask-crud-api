# Flask CRUD API 🧩

Este projeto é uma API RESTful simples desenvolvida com Flask, que permite **criar, ler, atualizar e deletar tarefas** — um exemplo prático de CRUD (Create, Read, Update, Delete).

## 📌 Objetivo

O objetivo deste projeto é consolidar os conceitos de back-end e rotas REST usando Flask e aplicar boas práticas de desenvolvimento de APIs.

---

## 🔧 Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- JSON (como formato de resposta)
- `pytest` (opcional para testes)

---

## 🚀 Como executar o projeto

### ✅ Pré-requisitos

- Python instalado
- pip instalado

### ▶️ Passos


# Clone o repositório (ou baixe)
git clone https://github.com/TAndressa/flask-crud-api

# Acesse a pasta do projeto

```bash
cd flask-crud-api
```

# Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # No Windows
source venv/bin/activate  # No macOS/Linux
```
# Instale as dependências

```bash
pip install flask
```
# Rode a aplicação

```bash
python app.py
```

# A API estará disponível em:
📍 http://localhost:5000/


### 📬 Rotas da API
| Método | Rota            | Descrição                     |
| ------ | --------------- | ----------------------------- |
| GET    | `/tarefas`      | Lista todas as tarefas        |
| GET    | `/tarefas/<id>` | Retorna uma tarefa específica |
| POST   | `/tarefas`      | Cria uma nova tarefa          |
| PUT    | `/tarefas/<id>` | Atualiza uma tarefa existente |
| DELETE | `/tarefas/<id>` | Deleta uma tarefa pelo ID     |

## 🧪 Testes (opcional)
Caso você deseje adicionar testes, pode seguir a mesma estrutura do projeto anterior com pytest.

## 📁 Estrutura do Projeto

flask-crud-api/
│
├── app.py               # Código principal da API
├── requirements.txt     # Dependências (atualize com pip freeze)
├── .gitignore           # Arquivos ignorados no controle de versão
└── README.md            # Este arquivo
