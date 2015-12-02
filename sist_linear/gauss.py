# coding: utf-8
'''
Created on Dec 1, 2015

@author: emanuele
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from sist_linear.subst_retro import substituicoes_retroativas

def gauss(n, A, b):
    '''
    Executa o método da eliminação de Gauss para resolver o sistema  linear Ax=b 
    transformando o sistema em um sistema triangular superior equivalente.
    Parâmetros de entrada: n: ordem da matriz A; A é uma matriz quadrada de 
    ordem n e b é o vetor constante.
    Saída: vetor x
    '''   
    # escreva o código aqui
    for k in range(0,n-1):
        for i in range(k+1,n):
            m = A[i][k]/A[k][k]
            A[i][k] = 0
            for j in range(k+1,n):
                A[i][j] = m * A[k][j] + A[i][j]
            b[i] = m * b[k] + b[i]

    x = substituicoes_retroativas(n, A, b)
    return x

if __name__ == "__main__":
    
    def teste01():
        n1 = 3
        A1 = [[1, -3, 2],
              [-2, 8, -1],
              [4, -6, 5]]
        b1 = [11, -15, 29]
        x = gauss(n1, A1, b1)
        if x != [2, -1, 3]:
            print("A função retornou um resultado não esperado. ")
            print("A solução deveria ser %s e o que foi retornado foi %s."%([2, -1, 3],x))
        else:
            print("Teste 1 bem sucedido")
            
    print("Testando o método da eliminação de gauss")
    teste01()
