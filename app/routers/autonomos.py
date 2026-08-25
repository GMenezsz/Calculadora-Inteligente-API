from fastapi import APIRouter, HTTPException
from typing import  Optional
from calculadora import *

router = APIRouter()

@router.post("/calculadora_autonomos")
def api_calculadora_autonomos(custos_operacionais: List[float], horas_trabalho: float, valor_hora: float, margem_lucro: float, taxa_maquininha: Optional[float] = None, deslocamento: Optional [list[float]] = None, custo_insumos: Optional [list[float]] = None):

    if validar_custos_operacionais(custos_operacionais) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_horas_trabalho(horas_trabalho) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_valor_hora(valor_hora) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_margem_lucro(margem_lucro) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_taxa_maquininha(taxa_maquininha) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_deslocamento(deslocamento) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    elif validar_custo_insumos(custo_insumos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
    else:
        resultado = calcular_custos(custos_operacionais=custos_operacionais, horas_trabalho=horas_trabalho, valor_hora=valor_hora, margem_lucro=margem_lucro, taxa_maquininha=taxa_maquininha, deslocamento=deslocamento, custo_insumos=custo_insumos)
        return {"resultado": resultado}