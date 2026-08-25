def calcular_alcool_gasolina(preco_alcool: float, preco_gasolina: float):
    if preco_alcool <= 0 or preco_gasolina <= 0:
        raise ValueError("Os valores não podem ser zero ou negativos.")
    
    resultado = preco_alcool / preco_gasolina

    if resultado < 0.7:
        melhor_opcao = "Álcool"
    else:
        melhor_opcao = "Gasolina"

    return {
        "resultado": round(resultado * 100, 2),
        "melhor_opcao": melhor_opcao
    }

def validar_alcool(preco_alcool: float):
    if preco_alcool <= 0:
        return False
    else:
        return True

def validar_gasolina(preco_gasolina: float):
    if preco_gasolina <= 0:
        return False
    else:
        return True