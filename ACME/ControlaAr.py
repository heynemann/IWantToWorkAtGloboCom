#!/usr/bin/env python
# encoding: utf-8
"""
ControlaAr.py

Created by Fernando Cezar on 2011-05-26.
"""


def main(argv):
    temperatura_inicial = 30
    temperatura_atual = 30
    temperatura_desejada = 20
    tempo_total = 360
    
    controle = Controle(temperatura_inicial)
    
    for tempo in range(tempo_total):
      estado_atual = controle.refrigera(temperatura_atual, temperatura_desejada)
      temperatura_atual = estado_atual[0]
                                             
    sys.stdout.write("Temperatura final: %.1f\nCusto: R$%.2f\n" % estado_atual)
    return 0




if __name__ == '__main__':
  import sys
  from Controle import Controle
  sys.exit(main(sys.argv))