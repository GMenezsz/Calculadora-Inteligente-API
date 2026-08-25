from calculadora import *
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/calculadora_juros_compostos")
def api_calculadora_juros_compostos(valor_inicial: float, aporte_mensal: float, taxa_juros: float, periodo_anos: int):
    if validar_valor_inicial(valor_inicial) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_aporte_mensal(aporte_mensal) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_taxa_juros(taxa_juros) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_periodo_anos(periodo_anos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calculadora_juros_compostos(valor_inicial=valor_inicial, aporte_mensal=aporte_mensal, taxa_juros=taxa_juros, periodo_anos=periodo_anos)
        return {"resultado": resultado}