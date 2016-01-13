# coding: utf-8

import sys
sys.path.append("../")


def trapz(x, y):
    """
    Aproxima o valor da integral pela regra do trapézio, onde x é um vetor
    contendo x0 e x1 e y é um vetor contendo f(x0) e f(x1).
    Retorna o valor da integral.
    
    """
    h = x[1] - x[0]
    T = (h/2) * (y[0] + y[1])
    
    return T

if __name__ == "__main__":
    x = [1,7]
    y = [1/1,1/7]
    T = trapz(x,y)
    print(T)