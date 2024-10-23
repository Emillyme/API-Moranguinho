from fastapi import FastAPI, Depends, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from model import Personagem, PersonagemDB
from sqlalchemy.orm import Session
from databaseConfig import engine, get_db
import uvicorn

# Inicializa o banco de dados criando as tabelas
PersonagemDB.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)

@app.get('/')
async def get_data():
    return {'body': 'Emilly ama comer tomate que nem maçã'}


@app.get('/personagens', response_model=list[Personagem])
async def get_personagens(db: Session = Depends(get_db)):
    personagens = db.query(PersonagemDB).all()
    return personagens


@app.get('/personagens/{personagem_id}', response_model=Personagem)
async def get_personagem(personagem_id: int, db: Session = Depends(get_db)):
    personagem = db.query(PersonagemDB).filter(PersonagemDB.id == personagem_id).first()
    if personagem:
        return personagem
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


@app.post('/personagens')
async def add_personagem(p: Personagem, db: Session = Depends(get_db)):
    db_personagem = PersonagemDB(**p.dict(exclude_unset=True))
    db.add(db_personagem)
    db.commit()
    db.refresh(db_personagem)
    return db_personagem

@app.put('/personagens/{personagem_id}', response_model=Personagem)
async def put_personagem(personagem_id: int, p: Personagem, db: Session = Depends(get_db)):
    personagem = db.query(PersonagemDB).filter(PersonagemDB.id == personagem_id).first()
    if personagem:
        for key, value in p.dict(exclude_unset=True).items():
            setattr(personagem, key, value)
        db.commit()
        db.refresh(personagem)
        return personagem
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


@app.delete('/personagens/{personagem_id}')
async def del_personagem(personagem_id: int, db: Session = Depends(get_db)):
    personagem = db.query(PersonagemDB).filter(PersonagemDB.id == personagem_id).first()
    if personagem:
        db.delete(personagem)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")


@app.patch('/personagens/{personagem_id}', response_model=Personagem)
async def patch_personagem(personagem_id: int, p: Personagem, db: Session = Depends(get_db)):
    personagem = db.query(PersonagemDB).filter(PersonagemDB.id == personagem_id).first()
    
    if personagem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    
    # Atualiza apenas os campos fornecidos no request
    for key, value in p.dict(exclude_unset=True).items():
        setattr(personagem, key, value)
    
    db.commit()
    db.refresh(personagem)  # Atualiza o personagem após o commit para garantir os dados atualizados
    return personagem


if __name__ == '__main__':
    uvicorn.run(app, port=9000)

    