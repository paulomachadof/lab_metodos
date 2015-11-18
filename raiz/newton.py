# coding: utf-8
'''
Created on Nov 9, 2015

@author:
'''
from math import *

def newton(f, df, x0, epsilon, maxIter = 50):
    """Executa o método de Newton a para achar o zero de f 
       com precisão epsilon. O método executa no máximo maxIter
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
   #Testando se X0 já é raiz    
    if abs(f(x0)) <= epsilon:
        return (False, x0)
   
    print("K\t      X\t             F(x)")

    for k in range(1, maxIter+1):
        x1 = x0 - f(x0)/df(x0)
        ## Mostra valores na tela
        print("%d\t %e\t %e"%(k,x1,f(x1)))
    
        ## Teste do critério de parada módulo da função
        if abs(f(x1)) <= epsilon:
            return (False, x1)
        x0 = x1

    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    print("O Número máximo de interações foi atingido")
    return(True, x1)
    
if __name__ == "__main__":
    
    def f(x):
        return x**3-9*x+3
    def df(x):
        return 3*x**2-9
    x0 = 0.5
    epsilon = 0.0001
    maxIter = 20
    print("Método de Newton-Raphson")
    (houveErro, raiz) = newton(f,df,x0,epsilon)
    if houveErro:
        print("O Método de Newton-Raphson a retornou um erro.")
    if raiz is not None:	
        print("Raiz encontrada: %s"%raiz)
