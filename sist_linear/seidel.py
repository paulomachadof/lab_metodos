# coding: utf-8
'''
Created on 14 de dez de 2015

@author: emanuele
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
from sist_linear.norma import norma

sys.path.append("../")

def seidel(n,A,b,epsilon,iterMax=50):
    """Resolve o sistema linear Ax=b usando o método iterativo Gauss-Jacobi.
    O critério de parada utiliza a norma-infinito.
    Saída é o vetor x.
    
    """
    x = n*[0]
    v = n*[0]
    for i in range(0,n):
        for j in range (0,n):
            if (i != j):
                A[i][j] = -A[i][j]/A[i][i]
        b[i] = b[i]/A[i][i]
        A[i][i] = 0
    for k in range(1,iterMax):
        for i in range(0,n):
            soma = 0
            for j in range(0,n):
                soma += A[i][j]*x[j]
            v[i] = x[i]
            x[i] = soma + b[i]
        
        d = norma(n,x,v)
        if(d < epsilon):
            return x
        for i in range(0,n):
            v[i] = x[i]
            
    print("O Número máximo de interações foi atingido")
if __name__ == "__main__":
    ## teste da função
    n = 3
    A =[[10, 3, -2],
        [2, 8, -1],
        [1, 1, 5]]
    b = [57,20,-4]
    epsilon = 0.05
    print("Testando o método de Gauss-Seidel para sistemas lineares")
    x = seidel(n,A,b,epsilon)
    print("x = %s"%x)