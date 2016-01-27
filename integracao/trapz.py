# coding: utf-8

import sys
sys.path.append("../")
from integracao.popula import popula_vetores

def trapz(x, y,m):
    """
    Aproxima o valor da integral pela regra do trapézio, onde x é um vetor
    contendo x0 e x1 e y é um vetor contendo f(x0) e f(x1).
    Retorna o valor da integral.
    """
    if len(x) != m+1 or len(y) != m+1:
        print("Erro!")
        return None
    
    h = (x[m] - x[0]) / m
    s = 0.0
    for i in range(1, m):
        s += y[i]
    It= (2 * s + y[0] + y[m]) * h/2
    return It

if __name__ == "__main__":
    from math import log
    
    def f(x):
        return x**3 * log(x)
    a = 1
    b = 3
    m = 4
    (x,y) = popula_vetores(f, a, b, m)
    T = trapz(x,y,m)
    print(T)