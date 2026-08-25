from fastapi import APIRouter, HTTPException
from typing import  Optional
from calculadora import *

router = APIRouter()

@router.post("/calculadora_motorista")
def api_calculadora_motorista(distancia: float, ganhos: float, consumo_veiculo: float, valor_combustivel: float, alimentacao: Optional[float] = None, cafe: Optional[float] = None, outros_gastos: Optional[float] = None):

    if validar_distancia(distancia) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.") 
    elif validar_consumo_veiculo(consumo_veiculo) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_valor_combustivel(valor_combustivel) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_ganhos(ganhos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_alimentacao(alimentacao) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_cafe(cafe) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_outros_gastos(outros_gastos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calculadora_motorista(distancia=distancia, ganhos=ganhos, consumo_veiculo=consumo_veiculo, valor_combustivel=valor_combustivel, alimentacao=alimentacao, cafe=cafe, outros_gastos=outros_gastos)

        ganhos_km = resultado["ganhos_por_km"]
        resultado_desempenho = resultado_quilometragem(ganhos_km)
        return {"resultado": resultado,
                "desempenho": resultado_desempenho}
