from pydantic import BaseModel
from typing import Union, Optional

class Personagem(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    idade: Optional[int] = None
    genero: Optional[str] = None
    objetivo: Optional[str] = None
    gosta: Optional[Union[str, None]] = None
    nao_gosta: Optional[Union[str, None]] = None
