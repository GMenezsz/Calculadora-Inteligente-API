from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class AlcoolGasolinaRequest(BaseModel):
    valor_alcool: float
    valor_gasolina: float

@router.post("/calculadora_alcool_gasolina")
def api_alcool_gasolina(dados: AlcoolGasolinaRequest):
    if validar_alcool(dados.valor_alcool) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_gasolina(dados.valor_gasolina) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_alcool_gasolina(
            preco_alcool=dados.valor_alcool, 
            preco_gasolina=dados.valor_gasolina
        )
        return {"resultado": resultado}
