==============  To-Do List API — Desafio Profissional (FastAPI + SQLite)  ============== 

Projeto final da máteria de Desafio Profissiol V:

A solução consiste em uma API de Gerenciamento de Tarefas (To-Do List) com CRUD completo, persistência em banco SQLite, documentação automática, testes básicos e um front-end simples para interação visual.

Obrigado Professor Cidão! :D

Links importantes

Documentação do Projeto :
https://docs.google.com/document/d/1--3VBnlqUOJFJT-mB-1UEb9Ecyb9AqvnpmFZFwgRPNE/edit?usp=sharing

Repositório do Projeto:
https://github.com/lucasl1803/todolist-dp

-> Tecnologias Utilizadas

Python 
FastAPI 
Uvicorn 
SQLite 
SQLAlchemy 
Pydantic 
HTML + CSS + JavaScript
Swagger UI / Redoc 

-> Como Executar o Projeto

1. Instale as dependências
pip install fastapi uvicorn sqlalchemy pydantic

2. Ative o ambiente virtual
.\venv\Scripts\Activate.ps1

3. Rode a API
uvicorn main:app --reload

API estará disponível em:

 http://127.0.0.1:8000

http://127.0.0.1:8000/docs
 (Swagger)

 http://127.0.0.1:8000/redoc

-> Front-end 

O arquivo index.html funciona como uma mini interface gráfica para:

Criar, listar e deletar as tarefas

-> Teste Básico Automatizado

O projeto possui um teste básico usando TestClient

-> Persistência de Dados

Toda a persistência utiliza SQLite, com mapeamento via SQLAlchemy.
O arquivo do banco é gerado automaticamente.

Lucas Leal Cardoso


