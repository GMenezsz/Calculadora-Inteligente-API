from calculadora import *
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/calculadora_combustivel")
def api_calculadora_combustivel(distancia: float, consumo_medio_kml: float, valor_combustivel: float):
    if validar_distancia(distancia) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_consumo_medio_kml(consumo_medio_kml) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_valor_combustivel(valor_combustivel) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_consumo_combustivel(distancia=distancia, consumo_medio_kml=consumo_medio_kml, valor_combustivel=valor_combustivel)
        return {"resultado": resultado}