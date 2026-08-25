from calculadora import *
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/calculadora_alcool_gasolina")
def api_alcool_gasolina(valor_alcool: float, valor_gasolina: float):

    if validar_alcool(valor_alcool) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_gasolina(valor_gasolina) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_alcool_gasolina(preco_alcool=valor_alcool, preco_gasolina=valor_gasolina)
        return {"resultado": resultado}