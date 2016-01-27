# coding: utf-8          

import sys
sys.path.append("../")

from interpolacao.poli_aval import poli_aval
from interpolacao.poli_lagrange import interpola_lagrange

def questao1():
    '''
    Como é interpolação cúbica, utilizaremos
    4 pontos.
    '''
    x = [15, 20, 25,30]
    y = [9.03, 8.17, 7.46, 6.85]
    n = 3
    p = interpola_lagrange(x, y, n)
    v = poli_aval(p, 23)
    print("1.Questão) ")
    print(v)
questao1()
#Resposta: 7.729200000000069