from pydantic import BaseModel
from typing import Union, Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para o SQLAlchemy
Base = declarative_base()

# Modelo para o SQLAlchemy (banco de dados)
class PersonagemDB(Base):
    __tablename__ = 'personagens'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    genero = Column(String)
    objetivo = Column(String)
    gosta = Column(String)
    nao_gosta = Column(String)
    imagem = Column(String)

# Modelo para Pydantic (validação da API)
class Personagem(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    idade: Optional[int] = None
    genero: Optional[str] = None
    objetivo: Optional[str] = None
    gosta: Optional[str] = None
    nao_gosta: Optional[str] = None
    imagem: Optional[str] = None