from typing import List, Optional

def calcular_media(prova_parcial: float, prova_global: float, trabalhos: Optional [list[float]] = None, pontos_extras: Optional [list[float]] = None):

    if trabalhos:
        total_trabalhos = sum(trabalhos)
    else:
        total_trabalhos = 0.0

    if pontos_extras:
        total_pontos_extras = sum(pontos_extras)
    else:
        total_pontos_extras = 0.0

    nota_base = (prova_parcial + prova_global) / 2
    nota_final = nota_base + total_trabalhos + total_pontos_extras


    return {
        "prova_parcial": round(prova_parcial, 2),
        "prova_global": round(prova_global, 2),
        "total_trabalhos_somado": round(total_trabalhos, 2),
        "total_pontos_extras": round(total_pontos_extras, 2),
        "nota_final": round(nota_final, 2),
        "aprovado": nota_final >= 60,
        "recuperacao": nota_final < 60
    }

def validar_parcial(prova_parcial: float):
    if prova_parcial < 0:
        return False
    else:
        return True

def validar_global(prova_global: float):
    if prova_global < 0:
        return False
    else:
        return True

def validar_pontos_extras(pontos_extras: Optional[List[float]]) -> bool:
    if not pontos_extras:
        return True
        
    for ponto in pontos_extras:
        if ponto < 0:
            return False       
    return True

def validar_trabalhos(trabalhos: Optional[List[float]]) -> bool:
    if not trabalhos:
        return True
        
    for ponto in trabalhos:
        if ponto < 0:
            return False       
    return True