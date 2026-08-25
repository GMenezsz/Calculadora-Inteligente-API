def calcular_gastos(potencia: int, horas_uso: float, dias_uso: int, valor_kwh: float):

    horas = int(horas_uso)
    minutos = int((horas_uso - horas) * 60)

    consumo_kwh = (potencia * horas_uso * dias_uso) / 1000
    custo_total = consumo_kwh * valor_kwh

    return {
        "consumo_energia_kwh": round(consumo_kwh, 2),
        "custo_total_R$": round(custo_total, 2),
        "horas_uso": horas,
        "minutos_uso": minutos,
        "dias_uso": dias_uso
    }

def validar_potencia(potencia: int):
    if potencia < 0:
        return False
    else:
        return True

def validar_horas_uso(horas_uso: float):
    if horas_uso < 0:
        return False
    else:
        return True

def validar_dias_uso(dias_uso: int):
    if dias_uso < 0:
        return False
    else:
        return True

def validar_valor_kwh(valor_kwh: float):
    if valor_kwh < 0:
        return False
    else:
        return True