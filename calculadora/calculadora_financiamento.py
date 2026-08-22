
def calcular_financiamento(valor_produto, taxa_juros, anos, valor_entrada=0):
    valor_financiado = valor_produto - valor_entrada
    juros_mensal = taxa_juros / 100
    prazo_anos = int(anos * 12) 

    fator = (1 + juros_mensal) ** prazo_anos
    parcela_mensal = (valor_financiado * (fator * juros_mensal)) / (fator - 1)

    valor_total = (parcela_mensal * prazo_anos) + valor_entrada
    total_juros = (parcela_mensal * prazo_anos) - valor_financiado

    return {
        "Parcela mensal": round(parcela_mensal, 2),
        "Valor entrada": round(valor_entrada, 2),
        "Valor total": round(valor_total, 2),
        "Valor total de juros": round(total_juros, 2),
        "Prazo em meses": prazo_anos 
    }

def validar_valor(valor):
    if valor <= 0:
        return False
    else:
        return True

def validar_juros(taxa_juros):
    if taxa_juros < 0:
        return False
    else:
        return True
    
def validar_entrada(valor_produto, valor_entrada):
    if valor_entrada < 0:
        return False
    
    elif valor_entrada >= valor_produto:
        return False
    
    else:
        return True

def validar_prazo(meses):
    if meses < 1:
        return False
    else: 
        return True
