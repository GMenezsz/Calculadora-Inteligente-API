from typing import List, Optional

def calcular_media_ponderada(
    prova_parcial: float,
    prova_global: float,
    trabalhos: Optional[list[float]] = None,
    pontos_extras: Optional[list[float]] = None,
):
  if trabalhos:
    media_trabalhos = sum(trabalhos) / len(trabalhos)
  else:
    media_trabalhos = 0.0
  if pontos_extras:
    total_pontos_extras = sum(pontos_extras)
  else:
    total_pontos_extras = 0.0

  nota_base_provas = (prova_parcial + prova_global) / 2

  if trabalhos:
    nota_final = (nota_base_provas * 0.6) + (media_trabalhos * 0.4)
  else:
    nota_final = nota_base_provas

  nota_final = min(nota_final + total_pontos_extras, 10.0)

  status_aluno = situacao_academica(nota_final)

  return {
      "nota_final": round(nota_final, 2),
      "situacao": status_aluno,
  }

def situacao_academica(nota_final: float):
    if nota_final >= 6.0:
        return "Aluno aprovado"
    else:
        return "Aluno reprovado / recuperação"

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
