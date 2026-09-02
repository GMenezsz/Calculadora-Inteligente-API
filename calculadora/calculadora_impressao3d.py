from typing import Optional

def calcular_custos_impressao(
        filamento_g: float,
        preco_filamento_kg: float,
        tempo_impressao: str,
        custo_energia: float,
        custo_maquina: float,
        margem_lucro_percentual: Optional[float],
        insumos: Optional[list[float]] = None,
        taxa_maquininha: Optional[float] = None,
        deslocamento_entrega: Optional[float] = None):
    
    if insumos is None:
        insumos = []

    if taxa_maquininha is None:
        taxa_maquininha = 0.0

    if deslocamento_entrega is None:
        deslocamento_entrega = 0.0

    if margem_lucro_percentual is None:
        margem_lucro_percentual = 0.0

    horas, minutos = map(int, tempo_impressao.split(":"))
    hora_decimal = horas + (minutos / 60)

    custo_filamento = (filamento_g / 1000) * preco_filamento_kg
    custo_energia_total = hora_decimal * custo_energia
    custo_maquina_total = hora_decimal * custo_maquina

    custo_total = custo_filamento + custo_energia_total + custo_maquina_total

    if insumos:
        custo_total += sum(insumos)

    if deslocamento_entrega:
        custo_total += deslocamento_entrega

    margem_decimal = margem_lucro_percentual / 100
    taxa_decimal = taxa_maquininha / 100

    divisor = 1.0 - margem_decimal - taxa_decimal

    if divisor <= 0:
        raise ValueError("A soma da margem de lucro e da taxa da maquininha não pode ser maior ou igual a 100%.")

    preco_sugerido = custo_total / divisor

    return {
        "preco_sugerido": round(preco_sugerido, 2),
        "custo_energia": round(custo_energia_total, 2),
        "custo_maquina": round(custo_maquina_total, 2),
        "custo_total": round(custo_total, 2),
        "lucro_liquido": round(preco_sugerido * margem_decimal, 2)
    }

def validar_filamento_g(preco):
    if preco <= 0:
        return False
    else:
        return True

def validar_filamento_kg(preco):
    if preco < 0:
        return False
    else:
        return True

def validar_tempo_impressao(tempo_impressao: str):
  try:
    horas, minutos = map(int, tempo_impressao.split(":"))

    if horas < 0 or minutos < 0 or minutos >= 60:
      return False
    
  except (ValueError, IndexError):
    raise ValueError("Formato de tempo inválido. Use o formato HH:MM (ex: 02:46).")
  return True

def validar_custo_energia(custo_energia):
    if custo_energia < 0:
        return False
    else:
        return True

def validar_custo_maquina(custo_maquina):
    if custo_maquina < 0:
        return False
    else:
        return True

def validar_margem_lucro(lucro: Optional[float]):
    if lucro is None:
        return True
    elif lucro < 0 or lucro >= 100:
        return False
    else:
        return True

def validar_insumos(insumos: Optional[list[float]]):
    if not insumos:
        return True
    
    for item in insumos:
        if item < 0:
            return False
    else:
        return True

def validar_taxa_maquininha(taxa_maquininha: Optional[float]):
    if taxa_maquininha is None:
        return True
    elif taxa_maquininha < 0:
        return False
    else:
        return True

def validar_deslocamento(deslocamento_entrega: Optional[float]):
    if deslocamento_entrega is None:
        return True
    elif deslocamento_entrega < 0:
        return False
    else:
        return True
