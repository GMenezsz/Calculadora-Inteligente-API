from fastapi import APIRouter, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class AutonomosRequest(BaseModel):
    custos_operacionais: Optional[List[float]] = None
    horas_trabalho: float
    valor_hora: float
    margem_lucro: float
    taxa_maquininha: Optional[float] = None
    deslocamento: Optional[List[float]] = None
    custo_insumos: Optional[List[float]] = None

@router.post("/calculadora_autonomos")
def api_calculadora_autonomos(dados: AutonomosRequest):
    
    if validar_custos_operacionais(dados.custos_operacionais) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_horas_trabalho(dados.horas_trabalho) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_valor_hora(dados.valor_hora) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_margem_lucro(dados.margem_lucro) is not True:
        raise HTTPException(status_code=400, detail="A margem de lucro deve ser entre 0 e 99.99%.")
        
    if validar_taxa_maquininha(dados.taxa_maquininha) is not True:
        raise HTTPException(status_code=400, detail="A taxa da maquininha deve ser entre 0 e 99.99%.")
        
    if validar_deslocamento(dados.deslocamento) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_custo_insumos(dados.custo_insumos) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    else:
        try:
            resultado = calcular_custos(
                custos_operacionais=dados.custos_operacionais,
                horas_trabalho=dados.horas_trabalho,
                valor_hora=dados.valor_hora,
                margem_lucro=dados.margem_lucro,
                taxa_maquininha=dados.taxa_maquininha,
                deslocamento=dados.deslocamento,
                custo_insumos=dados.custo_insumos
            )
        except ValueError as erro:
            raise HTTPException(status_code=400, detail=str(erro))
        return {"resultado": resultado}
