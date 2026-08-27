from calculadora import *
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class RegraTresRequest(BaseModel):
    valor1: float
    valor2: float
    valor3: float

@router.post("/calculadora_regra_tres")
def api_calculadora_regra_tres(dados: RegraTresRequest):
    
    if validar_regra_tres(dados.valor1, dados.valor2, dados.valor3) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_regra_tres(valor1=dados.valor1, valor2=dados.valor2, valor3=dados.valor3)
        return {"resultado": resultado}
