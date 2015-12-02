# coding: utf-8
'''
Created on Nov , 11 2015

@author: paulomachado
'''
from math import *

def secante(f,x0, x1, epsilon, maxIter = 50):
    """Executa o método da Secante para achar o zero de f 
       com precisão epsilon. O método executa no máximo maxIter
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
   # Testando se X0 já é raiz    
    if abs(f(x0)) <= epsilon:
        return (False, x0)

   # Testando se X1 já é raiz
    if abs(f(x1)) <= epsilon:
        return (False, x1)
    
   # Mostrando Cabeçalho
    print("K\t     X\t           F(x)         ")

    for k in range(1, maxIter+1):
        x2 = x1 - f(x1)/(f(x1) - f(x0)) * (x1 - x0)
	
        # Mostra valores na tela
        print("%d\t %e\t %e\t"%(k,x2,f(x2)))
    
        # Teste do critério de parada módulo da função
        if abs(f(x2)) <= epsilon:
            return (False, x2)
        x0 = x1
        x1 = x2

    # Se chegar aqui é porque o número máximo de iterações foi atingido
    print("O Número máximo de interações foi atingido")
    return(True, x2)
    
if __name__ == "__main__":
                                       
    def f(x):
        return x**3-9*x+3
    x0 = 0
    x1 = 1
    epsilon = 0.0005
    maxIter = 20
    print("Método da Secante")
    (houveErro, raiz) = secante(f,x1,x0,epsilon)
    if houveErro:
        print("O Método da Secante a retornou um erro.")
    if raiz is not None:
        print("Raiz encontrada: %s"%raiz)
