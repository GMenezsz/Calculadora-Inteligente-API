from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *
from typing import Optional

router = APIRouter()

class ImpressaoRequest(BaseModel):
        filamento_g: float
        preco_filamento_kg: float
        tempo_impressao: str
        custo_energia: float
        custo_maquina: float
        margem_lucro_percentual: Optional[float] = None
        insumos: Optional[list[float]] = None
        taxa_maquininha: Optional[float] = None
        deslocamento_entrega: Optional[float] = None

@router.post("/calculadora_3d")
def api_calcular_impressao3d(dados: ImpressaoRequest):

        if validar_filamento_g(dados.filamento_g) is not True:
                raise HTTPException(status_code=400, detail="O valor das gramas do filamento não pode ser menor que 0.")

        if validar_filamento_kg(dados.preco_filamento_kg) is not True:
                raise HTTPException(status_code=400, detail="O valor do filamento em kg não pode ser menor que 0.")

        if validar_tempo_impressao(dados.tempo_impressao) is not True:
                raise HTTPException(status_code=400, detail="Formato de tempo inválido. Use o formato HH:MM (ex: 02:46).")

        if validar_custo_energia(dados.custo_energia) is not True:
                raise HTTPException(status_code=400, detail="O custo e energia não pode ser menor que 0.")

        if validar_custo_maquina(dados.custo_maquina) is not True:
                raise HTTPException(status_code=400, detail="O custo da maquina não pode ser menor que 0.")

        if validar_margem_lucro_impressao(dados.margem_lucro_percentual) is not True:
                raise HTTPException(status_code=400, detail="A margem de lucro não pode ser menor que 0 e nem maior ou igual a 100.")

        if validar_insumos(dados.insumos) is not True:
                raise HTTPException(status_code=400, detail="O valor dos insumos não pode ser menor que 0.")

        if validar_taxa_maquininha_impressao(dados.taxa_maquininha) is not True:
                raise HTTPException(status_code=400, detail="A taxa da maquininha não pode ser menor que 0.")

        if validar_deslocamento_impressao(dados.deslocamento_entrega) is not True:
                raise HTTPException(status_code=400, detail="O valor de deslocamento/entrega não pode ser menor que 0.")

        try:
                resultado = calcular_custos_impressao(
                        filamento_g=dados.filamento_g,
                        preco_filamento_kg=dados.preco_filamento_kg,
                        tempo_impressao=dados.tempo_impressao,
                        custo_energia=dados.custo_energia,
                        custo_maquina=dados.custo_maquina,
                        margem_lucro_percentual=dados.margem_lucro_percentual,
                        insumos=dados.insumos,
                        taxa_maquininha=dados.taxa_maquininha,
                        deslocamento_entrega=dados.deslocamento_entrega
                )
        except ValueError as erro:
                raise HTTPException(status_code=400, detail=str(erro))

        return {"resultado": resultado}
