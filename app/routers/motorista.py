from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class MotoristaRequest(BaseModel):
    distancia: float
    ganhos: float
    consumo_veiculo: float
    valor_combustivel: float
    alimentacao: Optional[float] = None
    cafe: Optional[float] = None
    outros_gastos: Optional[float] = None

@router.post("/calculadora_motorista")
def api_calculadora_motorista(dados: MotoristaRequest):
    
    if validar_distancia(dados.distancia) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.") 
        
    if validar_consumo_veiculo(dados.consumo_veiculo) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_valor_combustivel(dados.valor_combustivel) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_ganhos(dados.ganhos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_alimentacao(dados.alimentacao) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_cafe(dados.cafe) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_outros_gastos(dados.outros_gastos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    
    resultado = calculadora_motorista(
        distancia=dados.distancia, 
        ganhos=dados.ganhos, 
        consumo_veiculo=dados.consumo_veiculo, 
        valor_combustivel=dados.valor_combustivel, 
        alimentacao=dados.alimentacao, 
        cafe=dados.cafe, 
        outros_gastos=dados.outros_gastos
    )

    ganhos_km = resultado["ganhos_por_km"]
    resultado_desempenho = resultado_quilometragem(ganhos_km)
    return {
        "resultado": resultado,
        "desempenho": resultado_desempenho
    }
