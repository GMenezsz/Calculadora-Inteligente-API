from typing import List, Optional

def calcular_preco_simples(
    horas_trabalho: float,
    valor_hora: float,
    margem_lucro: float,
    custos_operacionais: Optional[List[float]] = None,
    deslocamento: Optional[List[float]] = None,
    custo_insumos: Optional[List[float]] = None
):

    total_operacional = sum(custos_operacionais or [0])
    total_deslocamento = sum(deslocamento or [0])
    total_insumos = sum(custo_insumos or [0])
    
    custo_material = total_operacional + total_deslocamento + total_insumos
    
  
    remuneracao = horas_trabalho * valor_hora
    
   
    lucro = custo_material * (margem_lucro / 100)
    
    preco = remuneracao + custo_material + lucro
    
    return {
        "remuneracao_R$": round(remuneracao, 2),
        "custo_material_R$": round(custo_material, 2),
        "lucro_R$": round(lucro, 2),
        "preco_sugerido_R$": round(preco, 2)
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

def validar_deslocamento(deslocamento: Optional[List[float]]) -> bool:
    if deslocamento is None or not deslocamento:
        return True
    for custo in deslocamento:
        if custo < 0:
            return False
    return True
    

def validar_custo_insumos(custo_insumos: Optional[List[float]]) -> bool:
    if custo_insumos is None or not custo_insumos:
        return True
    for custo in custo_insumos:
        if custo < 0:
            return False
    return True

def validar_custos_operacionais(custos_operacionais: Optional[List[float]]) -> bool:
    if custos_operacionais is None or not custos_operacionais:
        return True
    for custo in custos_operacionais:
        if custo < 0:
            return False
    return True

def validar_taxa_maquininha(taxa_maquininha: Optional[float]) -> bool:
    if taxa_maquininha is None:
        return True
    if taxa_maquininha < 0:
        return False
    return True
