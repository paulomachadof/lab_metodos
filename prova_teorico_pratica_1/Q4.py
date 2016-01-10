# coding: utf-8

import sys
sys.path.append("../")
from raiz.ponto_fixo import ponto_fixo

if __name__ == "__main__":
    
    def f(x):
        return x**3 - 2*x - 5
    def fint(x):
        return x**3 - x - 5	
    a = 1
    b = 3
    x0 = 1.5
    print("Método da Ponto Fixo")
    (houveErro, raiz) = ponto_fixo(f,fint,a,b,x0)
    if houveErro:
        print("O Método da Ponto Fixo retornou um erro.")
    if raiz is not None:
        print("Raiz encontrada: %s"%raiz)

'''
O Método do Ponto Fixo não converge no determinado intervalo
'''