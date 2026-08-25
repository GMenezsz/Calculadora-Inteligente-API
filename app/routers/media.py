from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class MediaRequest(BaseModel):
    prova_parcial: float
    prova_global: float
    trabalhos: Optional[list[float]] = None
    pontos_extras: Optional[list[float]] = None

@router.post("/calculadora_media")
def api_calculadora_media(dados: MediaRequest):
    if validar_parcial(dados.prova_parcial) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_global(dados.prova_global) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_trabalhos(dados.trabalhos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_pontos_extras(dados.pontos_extras) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_media(
            prova_parcial=dados.prova_parcial, 
            prova_global=dados.prova_global, 
            trabalhos=dados.trabalhos, 
            pontos_extras=dados.pontos_extras
        )
        return {"resultado": resultado}
