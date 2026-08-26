from fastapi import APIRouter, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from calculadora import *

router = APIRouter()

class AutonomosRequest(BaseModel):
    horas_trabalho: float
    valor_hora: float
    margem_lucro: float
    custos_operacionais: Optional [List[float]] = None
    taxa_maquininha: Optional[float] = None
    deslocamento: Optional[List[float]] = None
    custo_insumos: Optional[List[float]] = None

@router.post("/calculadora_autonomos")
def api_calculadora_autonomos(dados: AutonomosRequest):
    if validar_horas_trabalho(dados.horas_trabalho) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_valor_hora(dados.valor_hora) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if validar_margem_lucro(dados.margem_lucro) is not True:
        raise HTTPException(status_code=400, detail="Valores inválidos.")
        
    if dados.custos_operacionais is not None:
        if not validar_custos_operacionais(dados.custos_operacionais):
            raise HTTPException(status_code=400, detail="Custos operacionais inválidos.")
        
    if dados.taxa_maquininha is not None:
        if not validar_taxa_maquininha(dados.taxa_maquininha):
            raise HTTPException(status_code=400, detail="Taxa da maquininha inválida.")
        
    if dados.deslocamento is not None:
        if not validar_deslocamento(dados.deslocamento):
            raise HTTPException(status_code=400, detail="Deslocamento inválido.")
        
    if dados.custo_insumos is not None:
        if not validar_custo_insumos(dados.custo_insumos):
            raise HTTPException(status_code=400, detail="Custo de insumos inválido.")
    
    resultado = calcular_custos(
        horas_trabalho=dados.horas_trabalho,           
        valor_hora=dados.valor_hora,                   
        margem_lucro=dados.margem_lucro,               
        custos_operacionais=dados.custos_operacionais, 
        taxa_maquininha=dados.taxa_maquininha,         
        deslocamento=dados.deslocamento,               
        custo_insumos=dados.custo_insumos              
    )
    return {"resultado": resultado}
