from fastapi import FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from model import Personagem  # model
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)

personagens = [
    {"id": 1, "nome": "Aragorn", "idade": 87, "genero": "Masculino", "objetivo": "Ser Rei", "gosta": "Lutar", "nao_gosta": "Traição"},
    {"id": 2, "nome": "Frodo", "idade": 50, "genero": "Masculino", "objetivo": "Destruir o anel", "gosta": "Amigos", "nao_gosta": "O anel"},
    {"id": 3, "nome": "Legolas", "idade": 2931, "genero": "Masculino", "objetivo": "Proteger a Terra-média", "gosta": "Arco e flecha", "nao_gosta": "Orcs"}
]

@app.get('/')
async def get_data():
    return {'body': 'Emilly ama comer tomate que nem maçã'}


@app.get('/personagens', response_model=List[Personagem])
async def get_personagens():
    return personagens


@app.get('/personagens/{personagem_id}')
async def get_personagem(personagem_id: int):
    personagem = next((p for p in personagens if p['id'] == personagem_id), None)
    if personagem:
        return personagem
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


@app.post('/personagens')
async def add_personagem(p: Personagem):
    try: 
        next_id = len(personagens) + 1
        p.id = next_id
        personagens.append(p.dict())
        return p
    except KeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Já existe um personagem com esse ID')


@app.put('/personagens/{personagem_id}', response_model=Personagem)
async def put_personagem(personagem_id: int, p: Personagem): # Personagem: Model, onde a pessoa vai escrever
    for i, personagem in enumerate(personagens):
        if personagem['id'] == personagem_id:
            personagens[i] = p.dict()  # Atualiza o personagem
            p.id = personagem_id  # Mantém o ID
            return p
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


@app.delete('/personagens/{personagem_id}')
async def del_personagem(personagem_id: int):
    for i, personagem in enumerate(personagens):
        if personagem['id'] == personagem_id:
            del personagens[i]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


@app.patch('/personagens/{personagem_id}', response_model=Personagem)
async def patch_personagem(personagem_id: int, p: Personagem):
    for i, personagem in enumerate(personagens):
        if personagem['id'] == personagem_id:
            for key, value in p.dict(exclude_unset=True).items():  # para garantir que apenas os campos fornecidos sejam atualizados.
                                                                 # Sobre oq é key e value:  se a key é "nome", e o valor é "Aragorn"
                personagens[i - 1][key] = value
            return personagens[i - 1]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


if __name__ == '__main__':
    uvicorn.run(app, port=9000)

    