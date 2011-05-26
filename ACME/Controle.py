#!/usr/bin/env python
# encoding: utf-8
"""
Controle.py

Created by Fernando Cezar on 2011-05-26.
"""

from ArCondicionado import ArCondicionado


class Controle(object):
  def __init__(self, temperatura_inicial):
    self.ar_condicionado = ArCondicionado(temperatura_inicial)


  def refrigera(self, temperatura_atual, temperatura_desejada):
    """Reduz a temperatura se necessário"""
    
    if temperatura_atual >= temperatura_desejada + 2:
      while temperatura_atual >= temperatura_desejada -2:
        temperatura_atual = self.ar_condicionado.reduzUmGrau()
    else:
      temperatura_atual += 0.5
      self.ar_condicionado.temperatura_atual += 0.5
      
    return self.estadoAtual()
  

  def estadoAtual(self):
    return self.ar_condicionado.estadoAtual()
  
  