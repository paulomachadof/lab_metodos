# coding: utf-8
'''
Created on 8 de dez de 2015

@author: emanuele

Arquivo para usar o método da decomposição LU para resolver sistemas lineares.


'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from sist_linear.subst_retro import substituicoes_retroativas
from sist_linear.subst_suc import substituicoes_sucessivas
from sist_linear.lu import lu

def industria_grega():
    n1 = 4
    A1 = [[3, 2, 2,4],
        [2, 3, 1, 2],
        [4, 1, 3, 5],
        [1, 4, 4, 3]]
    b1 = [133,90,163,126]
    b2 = [163,110,196,181]
    
    (L,U) = lu(n1,A1)
    y = substituicoes_sucessivas(n1, L, b1)
    x = substituicoes_retroativas(n1, U, y)
    print("Na fábrica Alfa, serão produzidas %s %s %s e %s unidades dos produtos (1), (2), (3) e (4), respectivamente"%tuple(x))
    
    y = substituicoes_sucessivas(n1, L, b2)
    x = substituicoes_retroativas(n1, U, y)
    print("Na fábrica Alfa, serão produzidas %s, %s, %s e %s unidades dos produtos (1), (2), (3) e (4), respectivamente"%tuple(x))


industria_grega()





