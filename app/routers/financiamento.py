from fastapi import APIRouter, HTTPException
from typing import  Optional
from calculadora import *

router = APIRouter()

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