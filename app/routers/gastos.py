from fastapi import APIRouter, HTTPException
from typing import  Optional
from calculadora import *

router = APIRouter()

@router.post("/calculadora_gastos")
def api_gastos(salario_liquido: float, gastos_essenciais: float):
    if validar_salario(salario_liquido) is not True or validar_gastos(gastos_essenciais) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    resultado = calcular_orcamento_50_30_20(salario_liquido, gastos_essenciais)
    return {"resultado": resultado}


