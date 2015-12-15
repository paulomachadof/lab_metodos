# coding: utf-8
'''
Created on 14 de dez de 2015

@author: emanuele
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from sist_linear import norma

def jacobi(n,A,b,epsilon,iterMax=50):
    """Resolve o sistema linear Ax=b usando o método iterativo Gauss-Jacobi.
    O critério de parada utiliza a norma-infinito.
    Saída é o vetor x.
    
    """
    # escreva o seu código aqui
    

if __name__ == "__main__":
    ## teste da função
    #n = ...
    #A = ...
    #b = ...
    #epsilon = ...
    print("Testando o método de Gauss-Jacobi para sistemas lineares")
    #x = jacobi(...)
    #print("x = %s"%x)