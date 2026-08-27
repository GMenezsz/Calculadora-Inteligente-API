from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class GastosRequest(BaseModel):
    salario_liquido: float
    gastos_essenciais: float

@router.post("/calculadora_gastos")
def api_gastos(dados: GastosRequest):
    if validar_salario(dados.salario_liquido) is not True 
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    
    if validar_gastos(dados.gastos_essenciais) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    resultado = calcular_orcamento_50_30_20(dados.salario_liquido, dados.gastos_essenciais)
    return {"resultado": resultado}
