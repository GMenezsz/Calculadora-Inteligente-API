from typing import List, Optional

def calcular_custos(
    horas_trabalho: float,
    valor_hora: float,
    margem_lucro: float,
    custos_operacionais: Optional[List[float]] = None,
    taxa_maquininha: Optional[float] = None,
    deslocamento: Optional[List[float]] = None,
    custo_insumos: Optional[List[float]] = None
):
    if margem_lucro < 0 or margem_lucro >= 100:
        raise ValueError("A margem de lucro deve ser entre 0 e 99.99%")

    if taxa_maquininha is not None and (taxa_maquininha < 0 or taxa_maquininha >= 100):
        raise ValueError("A taxa da maquininha deve ser entre 0 e 99.99%")

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

    # Custo com insumos (materiais/produtos usados no serviço)
    custo_insumos_total = total_insumos

    # Quanto você quer receber pelo seu tempo
    mao_de_obra = horas_trabalho * valor_hora

    # Preço precisa cobrir: operacional + insumos + deslocamento + sua hora de trabalho
    base = total_operacional + custo_insumos_total + total_deslocamento + mao_de_obra

    fator_preco = 1 - (margem_lucro / 100) - (taxa_maquininha / 100)

    if fator_preco <= 0:
        raise ValueError(
            f"A combinação de margem de lucro ({margem_lucro}%) e taxa da maquininha "
            f"({taxa_maquininha}%) resulta em um preço inválido."
        )

    preco_sugerido = base / fator_preco
    valor_maquininha = preco_sugerido * (taxa_maquininha / 100)
    lucro_margem = preco_sugerido * (margem_lucro / 100)

    # O que você realmente embolsa no fim: sua hora trabalhada + a margem de lucro do negócio
    ganho_total = mao_de_obra + lucro_margem

    return {
        "preco_sugerido_R$": round(preco_sugerido, 2),
        "custo_operacional_R$": round(total_operacional, 2),
        "custo_material_R$": round(custo_insumos_total, 2),
        "deslocamento_R$": round(total_deslocamento, 2),
        "mao_de_obra_R$": round(mao_de_obra, 2),
        "taxa_maquininha_R$": round(valor_maquininha, 2),
        "lucro_R$": round(lucro_margem, 2),
        "ganho_total_R$": round(ganho_total, 2),
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
    if margem_lucro < 0 or margem_lucro >= 100:
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
    if taxa_maquininha < 0 or taxa_maquininha >= 100:
        return False
    return True
