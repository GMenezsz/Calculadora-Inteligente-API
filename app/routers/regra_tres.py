from calculadora import *
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/calculadora_regra_tres")
def api_calculadora_regra_tres(valor1: float, valor2: float, valor3: float):
    if validar_regra_tres(valor1, valor2, valor3) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_regra_tres(valor1=valor1, valor2=valor2, valor3=valor3)
        return {"resultado": resultado}