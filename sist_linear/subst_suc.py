# coding: utf-8
'''
Created on Dec 8, 2015

@author: emanuele
'''

def substituicoes_sucessivas(n, A, b):
    '''Executa o método das substituições sucessivas para resolver o sistema 
       linear triangular inferior Ax=b.
       Parâmetros de entrada: n: ordem da matriz A; A é uma matriz triangular
       inferior e b é o vetor constante. 
       Saída: vetor     x
    '''
    x = n * [0]
    x[0] = b[0] / A[0][0]
    for i in range(1,n):
        soma = 0
        for j in range(0,i):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma)/A[i][i]
    
    return x

if __name__ == "__main__":
    
    def teste01():
        n1 = 4
        A1 = [[2, 0, 0, 0],
              [3, 5, 0, 0],
              [1, -6, 8, 0],
              [-1, 4, -3, 9]]
        b1 = [4, 1, 48, 6]
        x = substituicoes_sucessivas(n1, A1, b1)
        if x != [2, -1, 5, 3]:
            print("A função retornou um resultado não esperado. ")
            print("A solução deveria ser %s e o que foi retornado foi %s."%([2, -1, 5, 3],x))
            print("Verifique o seu código e tente novamente.\n")
        else:
            print("Teste 1 bem sucedido")
            
    print("Testando o método das substituições sucessivas")
    teste01()