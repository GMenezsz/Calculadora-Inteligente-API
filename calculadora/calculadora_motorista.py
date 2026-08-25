from typing import Optional

def calculadora_motorista(distancia: float, ganhos: float, consumo_veiculo: float, valor_combustivel: float, alimentacao: Optional[float] = None, cafe: Optional[float] = None, outros_gastos: Optional[float] = None):

    if alimentacao is None:
        alimentacao = 0.0
    if cafe is None:
        cafe = 0.0
    if outros_gastos is None:
        outros_gastos = 0.0

    percurso = distancia / consumo_veiculo
    custo_total = percurso * valor_combustivel
    ganhos_km = ganhos / distancia
    lucro_liquido = ganhos - custo_total - alimentacao - cafe - outros_gastos


    return {
        "lucro_liquido": round(lucro_liquido, 2),
        "ganhos_por_km": round(ganhos_km, 2),
        "custo_total_combustivel": round(custo_total, 2),
        "combustivel_gasto_litros": round(percurso, 2),
        "alimentacao": round(alimentacao, 2),
        "cafe": round(cafe, 2),
        "outros_gastos": round(outros_gastos, 2)
    }

def resultado_quilometragem(ganhos_km: float):
    if ganhos_km >= 3.00:
        return "A quilometragem está excelente."
    elif ganhos_km >= 2.00:
        return "A quilometragem está ótima."
    elif ganhos_km >= 1.00:
        return "A quilometragem está boa."
    else:
        return "A quilometragem está baixa."


def validar_distancia(distancia: float):
    if distancia < 0:
        return False
    else:
        return True

def validar_ganhos(ganhos: float):
    if ganhos < 0:
        return False
    else:
        return True

def validar_consumo_veiculo(consumo_veiculo: float):
    if consumo_veiculo < 0:
        return False
    else:
        return True

def validar_valor_combustivel(valor_combustivel: float):
    if valor_combustivel < 0:
        return False
    else:
        return True

def validar_alimentacao(alimentacao: Optional[float]):
    if alimentacao is None:
        return True
    elif alimentacao < 0:
        return False
    else:
        return True

def validar_cafe(cafe: Optional[float]):
    if cafe is None:
        return True
    elif cafe < 0:
        return False
    else:
        return True

def validar_outros_gastos(outros_gastos: Optional[float]):
    if outros_gastos is None:
        return True
    elif outros_gastos < 0:
        return False
    else:
        return True