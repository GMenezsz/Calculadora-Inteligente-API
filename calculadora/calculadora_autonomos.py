from typing import List, Optional

def calcular_custos(horas_trabalho: float, valor_hora: float, margem_lucro: float, custos_operacionais: Optional[List[float]] = None, taxa_maquininha: Optional[float] = None, deslocamento: Optional[List[float]] = None, custo_insumos: Optional[list[float]] = None):


    if custos_operacionais is None:
        custos_operacionais = [0.0]
    if deslocamento is None:
        deslocamento = [0.0]
    if custo_insumos is None:
        custo_insumos = [0.0]
    if taxa_maquininha is None:
        taxa_maquininha = 0.0
        
    total_operacional = sum(custos_operacionais)
    total_deslocamento = sum(deslocamento)
    total_insumos = sum(custo_insumos)
    total_mao_de_obra = horas_trabalho * valor_hora

    custo_total = total_operacional + total_deslocamento + total_insumos + total_mao_de_obra

    fator_preco = 1 - (margem_lucro / 100) - (taxa_maquininha / 100)
    preco_sugerido = custo_total / fator_preco 
    lucro = preco_sugerido * (margem_lucro / 100) 


    return {
        "custo_total_R$": round(custo_total, 2),
        "preco_sugerido_R$": round(preco_sugerido, 2),
        "lucro_R$": round(lucro, 2),
    }

def validar_horas_trabalho(horas_trabalho: float):
    if horas_trabalho < 0:
        return False
    else:
        return True

def validar_valor_hora(valor_hora: float):
    if valor_hora < 0:
        return False
    else:
        return True

def validar_margem_lucro(margem_lucro: float):
    if margem_lucro < 0:
        return False
    else:
        return True

def validar_deslocamento(deslocamento: List[float]):
    if not deslocamento:
        return True
    for custo in deslocamento:
        if custo < 0:
            return False
    else:
        return True
    

def validar_custo_insumos(custo_insumos: List[float]):
    if not custo_insumos:
        return True
    for custo in custo_insumos:
        if custo < 0:
            return False
    else:
        return True

def validar_custos_operacionais(custos_operacionais: List[float]):
    if not custos_operacionais:
        return True
    for custo in custos_operacionais:
        if custo < 0:
            return False
    else:
        return True

def validar_taxa_maquininha(taxa_maquininha: float):
    if taxa_maquininha < 0:
        return False
    else:
        return True
