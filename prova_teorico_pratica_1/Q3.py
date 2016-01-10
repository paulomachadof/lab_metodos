# coding: utf-8

import sys
sys.path.append("../")

from raiz.newton import newton

def divide(b,a):
    def f(x):
        return a*x - b
    def df(x):  
        return a
    x0 = 0
    epsilon = 0.00000001
    (houveErro, raiz) = newton(f, df, x0, epsilon)
    if houveErro:
        print("O Método Retornou um Erro")
    if raiz is not None:
        print("Resultado da divisão: %s"%raiz)

divide(3,13)

'''
Resultado da divisão: 0.23076923076923078
'''