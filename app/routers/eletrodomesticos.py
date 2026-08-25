from fastapi import APIRouter, HTTPException
from calculadora import *

router = APIRouter()

@router.post("/calculadora_eletrodomesticos")
def api_calculadora_eletrodomesticos(potencia: int, horas_uso: float, dias_uso: int, valor_kwh: float):
    if validar_potencia(potencia) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_horas_uso(horas_uso) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_dias_uso(dias_uso) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_valor_kwh(valor_kwh) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_gastos(potencia=potencia, horas_uso=horas_uso, dias_uso=dias_uso, valor_kwh=valor_kwh)
        return {"resultado": resultado}