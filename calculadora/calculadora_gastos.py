def calcular_orcamento_50_30_20(salario_liquido, gastos_essenciais):
    porcentagem_gastos = (gastos_essenciais / salario_liquido) * 100
    
    valor_lazer_30 = salario_liquido * 0.30
    valor_guardar_20 = salario_liquido * 0.20
    
    return {
        "salario_liquido": round(salario_liquido, 2),
        "gastos_essenciais_percentual": round(porcentagem_gastos, 2),
        "valor_lazer_30": round(valor_lazer_30, 2),
        "valor_guardar_20": round(valor_guardar_20, 2),
        "porcentagem_dentro_limite": porcentagem_gastos <=50
    }

def validar_salario(salario):
    if salario < 0:
        return False
    else:
        return True

def validar_gastos(gastos_essenciais):
    if gastos_essenciais < 0:
        return False
    else:
        return True

