# coding: utf-8

import sys
sys.path.append("../")

from integracao.popula import popula_vetores

def simpson13(x, y, m=2):
    """
    Aproxima o valor da integral pela regra 1/3 de simpson repetida, onde x é 
    um vetor contendo os valores de xi, y é um vetor contendo os valores de 
    f(xi) e m é o número de subintervalos e deve ser par.
    
    Retorna o valor da integral.
    
    """
    
    if (m % 2 != 0):
        print("m não é PAR")
        return None
    s = 0.0
    h = (x[m]-x[0]) / m
    for i in range(0,m+1):
        if i == 0 or i == m:
            c = 1
        elif i % 2 == 0:
            c = 2
        else:
            c = 4
        print(i, c, y[i])
        s += c*y[i]
    return h/3 * s   
if __name__ == "__main__":
    from math import log
    def f(x):
        return x**3 * log(x)
    a = 1
    b = 3
    m = 4
    (x,y) = popula_vetores(f, a, b, m)
    S = simpson13(x,y,m)
    print(S)