def notas(
        caixa: Optional[float] = None,
        qtd_100: Optional[int] = None, 
        qtd_50: Optional[int] = None, 
        qtd_20: Optional[int] = None,
        qtd_10: Optional[int] = None,
        qtd_5: Optional[int] = None,
        qtd_2: Optional[int] = None,
        qtd_1: Optional[int] = None,
        saida: Optional[float] = None):

    if caixa is None:
        caixa = 0.0

    if qtd_100 is None:
        qtd_100 = 0.0

    if qtd_50 is None:
        qtd_50 = 0.0

    if qtd_20 is None:
        qtd_20 = 0.0

    if qtd_10 is None:
        qtd_10 = 0.0

    if qtd_5 is None:
        qtd_5 = 0.0

    if qtd_2 is None:
        qtd_2 = 0.0

    if qtd_1 is None:
        qtd_1 = 0.0

    if saida is None:
        saida = 0.0

    total100 = qtd_100 * 100
    total50 = qtd_50 * 50
    total20 = qtd_20 * 20
    total10 = qtd_10 * 10
    total5 = qtd_5 * 5
    total2 = qtd_2 * 2
    total1 = qtd_1 * 1
    caixa = caixa
    saida = saida

    total = total100 + total50 + total20 + total10 + total5 + total2 + total1 + caixa - saida
    return total


    
def validar_caixa(caixa: Optional[float]):
    if caixa is None:
        return True
    elif caixa < 0:
        return False
    else:
        return True

def validar_notas100(qtd_100: Optional[int]):  
    if qtd_100 is None:
        return True
    elif qtd_100 <= 0:
        return False
    else:
        return True

def validar_notas50(qtd_50: Optional[int]):  
    if qtd_50 is None:
        return True
    elif qtd_50 <= 0:
        return False
    else:
        return True

def validar_notas20(qtd_20: Optional[int]):  
    if qtd_20 is None:
        return True
    elif qtd_20 <= 0:
        return False
    else:
        return True

def validar_notas10(qtd_10: Optional[int]):  
    if qtd_10 is None:
        return True
    elif qtd_10 <= 0:
        return False
    else:
        return True

def validar_notas5(qtd_5: Optional[int]):  
    if qtd_5 is None:
        return True
    elif qtd_5 <= 0:
        return False
    else:
        return True

def validar_notas2(qtd_2: Optional[int]):  
    if qtd_2 is None:
        return True
    elif qtd_2 <= 0:
        return False
    else:
        return True

def validar_notas1(qtd_1: Optional[int]):  
    if qtd_1 is None:
        return True
    elif qtd_1 <= 0:
        return False
    else:
        return True

def validar_saida(saida: Optional[float]):
    if saida is None:
        return True
    elif saida <= 0:
        return False
    else:
        return True
