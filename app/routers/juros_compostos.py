from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class JurosCompostosRequest(BaseModel):
    valor_inicial: float
    aporte_mensal: float
    taxa_juros: float
    periodo_anos: int

@router.post("/calculadora_juros_compostos")
def api_calculadora_juros_compostos(dados: JurosCompostosRequest):
    if validar_valor_inicial(dados.valor_inicial) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_aporte_mensal(dados.aporte_mensal) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_taxa_juros(dados.taxa_juros) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_periodo_anos(dados.periodo_anos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calculadora_juros_compostos(
            valor_inicial=dados.valor_inicial, 
            aporte_mensal=dados.aporte_mensal, 
            taxa_juros=dados.taxa_juros, 
            periodo_anos=dados.periodo_anos
        )
        return {"resultado": resultado}
