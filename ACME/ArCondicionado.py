#!/usr/bin/env python
# encoding: utf-8

"""
ArCondicionado.py

Created by Fernando Cezar on 2011-05-26.
"""


class ArCondicionado(object):
  """Classe implementa as funções básicas de um
   Ar Condicionado padrão da ACME Corp."""
  
  def __init__(self, temperatura_inicial):
    self.temperatura_atual = temperatura_inicial
    self.compressor = {"ligado": False, "custo": 0.50}
    self.custo = 0  
  
  
  def reduzUmGrau(self):
    """Essa função reduz a temperatura atual em 1 grau, o custo do ar
    condicionado aumenta.
       O nome da função foi modificado para ficar de acordo com a PEP8.
    """
       
    if not self.compressor["ligado"]:
      self.compressor["ligado"] = True
      self.custo += self.compressor["custo"]
    
    self.temperatura_atual -= 1
    self.custo += 0.1
    return self.temperatura_atual
  
  
  
  def estadoAtual(self):
    """Retorna a tupla (temperatura atua, custo total)"""
    return (self.temperatura_atual, self.custo)
  