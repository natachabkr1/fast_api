# Criação do ambiente virtual: py -3 -m venv .venv
# Ativação do ambiente: .\.venv\Scripts\activate

# Instalação do FASTAPI: pip install "fastapi[all]"

# from fastapi import FastAPI
# from typing import Union  # ajuda a trabalhar com funções de mais de 1 tipo
# from pydantic import BaseModel


# app = FastAPI()

# class Item(BaseModel):   # criando uma classe para representar um item
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")   # criação da 1º rota
# async def root():
#     return {"message": "Olá, womakers!"}

# @app.get("/items/{item_id}")   # criação da 2º rota
# async def read_item(item_id: int, busca: Union[str, int] = None):
#     return {"item_id": item_id, "busca": busca}

# @app.put("/items/{item_id}")   
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item.id": item_id}

# No terminal - iniciar o servidor: uvicorn app:app --reload

from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(id=UUID("9e710b5c-0ae5-4e43-8a40-d8bc3662255b"), first_name="johndoe", last_name= "Margarita", email="john@example.com", role=[Role.role_1]),
    User(id=UUID("8a928e42-4ff6-401d-8bcc-2c210acf7f25"), first_name="Nati", last_name= "cigana", email="john@example.com", role=[Role.role_2]),
    User(id=UUID("69986ef9-266a-41a3-a43b-4296586110a7"), first_name="Fer", last_name= "redondo", email="john@example.com", role=[Role.role_3])
]

# GET

@app.get("/")   # criação da 1º rota
async def root():
    return {"message": "Olá, womakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado."}


# POST

@app.post("/api/users")
async def add_user(user: User):
    '''
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: str
    - **last_name**: str
    - **email**: str
    - **role**: List[Role]
    '''
    db.append(user)
    return {"id": user.id}


# DELETE

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(                     # EXCEPTIONS
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )




