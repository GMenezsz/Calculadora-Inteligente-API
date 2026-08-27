from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class CombustivelRequest(BaseModel):
    distancia: float
    consumo_medio_kml: float
    valor_combustivel: float

@router.post("/calculadora_combustivel")
def api_calculadora_combustivel(dados: CombustivelRequest):
    if validar_distancia(dados.distancia) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    if validar_consumo_medio_kml(dados.consumo_medio_kml) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    if validar_valor_combustivel(dados.valor_combustivel) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    
    resultado = calcular_consumo_combustivel(
        distancia=dados.distancia, 
        consumo_medio_kml=dados.consumo_medio_kml, 
        valor_combustivel=dados.valor_combustivel
    )
    return {"resultado": resultado}
