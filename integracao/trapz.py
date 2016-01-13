# coding: utf-8

import sys
sys.path.append("../")


def trapz(x, y, m=1):
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
    x = [1,7]
    y = [1/1,1/7]
    T = trapz(x,y)
    print(T)