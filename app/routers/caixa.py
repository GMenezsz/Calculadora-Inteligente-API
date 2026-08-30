from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from calculadora import *
from typing import Optional

router = APIRouter()

class CaixaRequest(BaseModel):
    caixa: Optional[float] = None
    qtd_100: Optional[int] = None
    qtd_50: Optional[int] = None
    qtd_20: Optional[int] = None
    qtd_10: Optional[int] = None
    qtd_5: Optional[int] = None
    qtd_2: Optional[int] = None
    qtd_1: Optional[int] = None
    saida: Optional[float] = None

@router.post("/calculadora_caixa")
def api_calcular_caixa(dados: CaixaRequest):
    if validar_caixa(dados.caixa) is not True:
        raise HTTPException(status_code=400, detail="O valor do caixa nao pode ser negativo.")

    if validar_notas100(dados.qtd_100) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de notas de R$100,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha notas de R$100,00.")

    if validar_notas50(dados.qtd_50) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de notas de R$50,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha notas de R$50,00.")

    if validar_notas20(dados.qtd_20) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de notas de R$20,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha notas de R$20,00.")

    if validar_notas10(dados.qtd_10) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de notas de R$10,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha notas de R$10,00.")

    if validar_notas5(dados.qtd_5) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de notas de R$5,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha notas de R$5,00.")

    if validar_notas2(dados.qtd_2) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de notas de R$2,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha notas de R$2,00.")

    if validar_notas1(dados.qtd_1) is not True:
        raise HTTPException(status_code=400, detail="A quantidade de moedas de R$1,00 não pode ser 0 ou negativo. Deixe o campo vazio caso nao tenha moedas de R$1,00.")

    if validar_saida(dados.saida) is not True:
        raise HTTPException(status_code=400, detail="O valor de saída não pode ser negativo.")

    resultado_total = notas(
        caixa=dados.caixa,
        qtd_100=dados.qtd_100,
        qtd_50=dados.qtd_50,
        qtd_20=dados.qtd_20,
        qtd_10=dados.qtd_10,
        qtd_5=dados.qtd_5,
        qtd_2=dados.qtd_2,
        qtd_1=dados.qtd_1,
        saida=dados.saida
    )

    return {
        "caixa_inicial": dados.caixa,
        "total_caixa": resultado_total}
