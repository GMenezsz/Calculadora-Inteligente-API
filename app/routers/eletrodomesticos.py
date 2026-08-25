from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class EletrodomesticosRequest(BaseModel):
    potencia: int
    horas_uso: float
    dias_uso: int
    valor_kwh: float

@router.post("/calculadora_eletrodomesticos")
def api_calculadora_eletrodomesticos(dados: EletrodomesticosRequest):
    if validar_potencia(dados.potencia) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_horas_uso(dados.horas_uso) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_dias_uso(dados.dias_uso) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_valor_kwh(dados.valor_kwh) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_gastos(
            potencia=dados.potencia, 
            horas_uso=dados.horas_uso, 
            dias_uso=dados.dias_uso, 
            valor_kwh=dados.valor_kwh
        )
        return {"resultado": resultado}
