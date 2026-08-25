def calcular_consumo_combustivel(distancia, consumo_medio_kml, valor_combustivel):
    percurso = distancia / consumo_medio_kml
    custo_total = percurso * valor_combustivel

    return {
        "combustivel_necessario": round(percurso, 2),
        "custo_total": round(custo_total, 2)  
    }

def validar_distancia(distancia):
    if distancia < 0:
        return False
    else:
        return True

def validar_consumo_medio_kml(consumo_medio_kml):
    if consumo_medio_kml < 0:
        return False
    else:
        return True

def validar_valor_combustivel(valor_combustivel):
    if valor_combustivel < 0:
        return False
    else:
        return True