# coding: utf-8
'''
Created on Nov 9, 2015

@author:
'''
from math import *

def newton_poli(n, a, x, epsilon, maxIter = 50):
    """Executa o método de Newton a para achar o zero de f 
       com precisão epsilon. O método executa no máximo maxIter
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    print("K\t      X\t             p(x)")

    for k in range(0, maxIter+1):
        b = a[n]
        c = b
        for i in range(n-1,0,-1):
            b = b*x+a[i]
            c = c*x+b
        b = b*x+a[0]
        ## Mostra valores na tela
        print("%d\t %e\t %e"%(k,x,b))
    
        ## Teste do critério de parada módulo da função
        if abs(b) <= epsilon:
            return (False, x)
        x = x - (b/c)
	
    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    print("O Número máximo de interações foi atingido")
    return(True, x)
    
if __name__ == "__main__":
    
    n = 3
    a = [-2, -1, 2, 1]
    x = 2
    epsilon = 0.01
    maxIter = 30
    print("Método de Newton Para Polinômios")
    (houveErro, raiz) = newton_poli(n,a,x,epsilon)
    if houveErro:
        print("O Método de Newton Para Zerar Polinômios a retornou um erro.")
    if raiz is not None:	
        print("Raiz encontrada: %s"%raiz)
