from typing import List, Optional

def calcular_media_ponderada(
    prova_parcial: float,
    prova_global: float,
    trabalhos: Optional[list[float]] = None,
    pontos_extras: Optional[list[float]] = None,
):
  # 1. Soma e média dos trabalhos (se existirem)
  if trabalhos:
    media_trabalhos = sum(trabalhos) / len(trabalhos)
  else:
    media_trabalhos = 0.0

  # 2. Soma dos pontos extras
  if pontos_extras:
    total_pontos_extras = sum(pontos_extras)
  else:
    total_pontos_extras = 0.0

  # 3. Média base das provas
  nota_base_provas = (prova_parcial + prova_global) / 2

  # 4. Aplicação dos pesos (Exemplo: Provas valem 60% / 0.6 e Trabalhos valem 40% / 0.4)
  if trabalhos:
    nota_final = (nota_base_provas * 0.6) + (media_trabalhos * 0.4)
  else:
    nota_final = nota_base_provas

  # Adiciona os pontos extras e garante que a nota final não passe de 10
  nota_final = min(nota_final + total_pontos_extras, 10.0)

  status_aluno = situacao_academica(nota_final)

  return {
      "nota_final": round(nota_final, 2),
      "situacao": status_aluno,
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
