def calcular_regra_tres(valor1: float, valor2: float, valor3: float):
    if valor1 <= 0 or valor2 <= 0 or valor3 <= 0:
        raise ValueError("Os valores não podem ser zero.")
    
    resultado = (valor2 * valor3) / valor1

    return {
        "valor_encontrada": round(resultado, 2)
    }

def validar_regra_tres(valor1: float, valor2: float, valor3: float):
    if valor1 <= 0 or valor2 <= 0 or valor3 <= 0:
        return False
    else:
        return True