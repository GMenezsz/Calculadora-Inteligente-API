from fastapi import APIRouter, HTTPException
from typing import  Optional
from calculadora import *

router = APIRouter()

@router.post("/calculadora_gastos")
def api_gastos(salario_liquido: float, gastos_essenciais: float):
    if validar_salario(salario_liquido) is not True or validar_gastos(gastos_essenciais) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    resultado = calcular_orcamento_50_30_20(salario_liquido, gastos_essenciais)
    return {"resultado": resultado}

@router.post("/Calculadora_financiamento")
def api_calculadora(valor: float, taxa_juros: float, ano: int, valor_entrada: Optional[float] = 0):


    if validar_valor(valor) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    if valor_entrada is None:
        valor_entrada = 0

    elif validar_entrada(valor, valor_entrada) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.") 

    elif validar_juros(taxa_juros) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    elif validar_prazo(ano * 12) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_financiamento(valor_produto=valor , taxa_juros=taxa_juros, anos=ano, valor_entrada=valor_entrada)
        return {"resultado": resultado}

@router.post("/calculadora_media")
def api_calculadora_media(prova_parcial: float, prova_global: float, trabalhos: Optional [list[float]] = None, pontos_extras: Optional [list[float]] = None):

    if validar_parcial(prova_parcial) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")

    elif validar_global(prova_global) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_trabalhos(trabalhos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_pontos_extras(pontos_extras) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_media(prova_parcial=prova_parcial, prova_global=prova_global, trabalhos=trabalhos, pontos_extras=pontos_extras)
        return {"resultado": resultado}
    
