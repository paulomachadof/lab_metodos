# coding: utf-8
'''
Created on 29 de dez de 2015

@author: paulomachado
'''
from math import *

def ponto_fixo(f,fint,a,b,x0, maxIter = 50):
    """Executa o método do Ponto Fixo a para achar o zero de f 
       no intervalo [a,b]. O método executa no máximo maxIter
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    #Testando se x0 já é raiz    
    if abs(f(x0)) < a:
        return (False, x0)
   
    print("K\t      X\t             F(x)")

    for k in range(1, maxIter+1):
        x1 = fint(x0)
        ## Mostra valores na tela
        print("%d\t %e\t %e"%(k,x1,f(x1)))
    
        ## Teste do critério de parada módulo da função
        if abs(f(x1)) < a or abs(x1- x0) < b:
            return (False, x1)
        x0 = x1

    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    print("O Número máximo de interações foi atingido")
    return(True, x1)
if __name__ == "__main__":
    
    def f(x):
        return x**9 - 9*x - 3
    def fint(x):
        return x**3/9 + 1/3	
    a = 5*10**-4
    b = 5*10**-4
    x0 = 0.5
    print("Método da Ponto Fixo")
    (houveErro, raiz) = ponto_fixo(f,fint,a,b,x0)
    if houveErro:
        print("O Método da Ponto Fixo retornou um erro.")
    if raiz is not None:
        print("Raiz encontrada: %s"%raiz)
