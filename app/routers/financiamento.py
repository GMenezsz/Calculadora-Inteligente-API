from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class FinanciamentoRequest(BaseModel):
    valor: float
    taxa_juros: float
    ano: int
    valor_entrada: Optional[float] = 0

@router.post("/calculadora_financiamento")
def api_calculadora(dados: FinanciamentoRequest):
    if validar_valor(dados.valor) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    entrada = 0 if dados.valor_entrada is None else dados.valor_entrada

    if dados.valor_entrada is not None and validar_entrada(dados.valor, dados.valor_entrada) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.") 
    elif validar_juros(dados.taxa_juros) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_prazo(dados.ano * 12) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_financiamento(
            valor_produto=dados.valor, 
            taxa_juros=dados.taxa_juros, 
            anos=dados.ano, 
            valor_entrada=entrada
        )
        return {"resultado": resultado}
