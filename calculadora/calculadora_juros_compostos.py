def calculadora_juros_compostos(valor_inicial, aporte_mensal, taxa_juros, periodo_anos):
    periodo_meses = periodo_anos * 12
    taxa_mensal = (taxa_juros / 100) / 12

    montante = float(valor_inicial)

    for mes in range(1, periodo_meses + 1):
        montante = (montante * (1 + taxa_mensal)) + aporte_mensal

    total_investido = valor_inicial + (aporte_mensal * periodo_meses)
    total_juros = montante - total_investido

    rentabilidade_total = 0.0  
    if total_investido > 0:
        rentabilidade_total = (total_juros / total_investido) * 100

    return {
        "resultado": {
            "montante_final": round(montante, 2),
            "total_investido": round(total_investido, 2),
            "juros_ganhos": round(total_juros, 2),
            "rentabilidade_total": round(rentabilidade_total, 2)
        }
    }

def validar_valor_inicial(valor_inicial):
    if valor_inicial <= 0:
        return False
    else:
        return True

def validar_aporte_mensal(aporte_mensal):
    if aporte_mensal <= 0:
        return False
    else:
        return True

def validar_taxa_juros(taxa_juros):
    if taxa_juros <= 0:
        return False
    else:
        return True

def validar_periodo_anos(periodo_anos):
    if periodo_anos <= 0:
        return False
    else:
        return True
