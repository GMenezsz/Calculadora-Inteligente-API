from fastapi import APIRouter, HTTPException
from typing import  Optional
from calculadora import *

router = APIRouter()

@router.post("/calculadora_media")
def api_calculadora_media(prova_parcial: float, prova_global: float, trabalhos: Optional [list[float]] = None, pontos_extras: Optional [list[float]] = None):

    if validar_parcial(prova_parcial) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    elif validar_global(prova_global) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_trabalhos(trabalhos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_pontos_extras(pontos_extras) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_media(prova_parcial=prova_parcial, prova_global=prova_global, trabalhos=trabalhos, pontos_extras=pontos_extras)
        return {"resultado": resultado}
    