# coding: utf-8
'''
Created on Dec 8, 2015

@author: emanuele
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from sist_linear.subst_suc import substituicoes_sucessivas
from sist_linear.subst_retro import substituicoes_retroativas


def identidade(n):
    """Retorna uma matriz identidade de ordem n.
    Saída matriz I
    """
    I = []
    for i in range(0,n):
        linha = n *[0]
        linha[i] = 1
        I.append(linha)
    return I

def lu(n, A):
    '''
    Decompõe a matriz A no produto de duas matrizes L e U. Onde L é uma matriz 
    triangular inferior unitária e U é uma matriz triangular superior.
    Parâmetros de entrada: n: ordem da matriz A, A é uma matriz quadrada de 
    ordem n.
    Saída: (L,U) tupla com as matrizes L e U
    '''
    #inicializa a matriz l com a matriz identidade
    L = identidade(n)
    
    #copie o código de gauss e modifique para a decomposição LU
    for k in range(0,n-1):
        for i in range(k+1,n):
            m = -A[i][k]/A[k][k]
            A[i][k] = 0
            L[i][k] = -m
            for j in range(k+1,n):
                A[i][j] = m * A[k][j] + A[i][j]
           
    #U será a matriz A modificada 
    return (L,A)

def resolve_lu(n,A,b):
    '''
    Executa o método LU para resolver o sistema  linear Ax=b.
    Esse método inicialmente decompõe a matriz em L e U e depois resolve os 
    dois sistemas lineares triangulares.
    Parâmetros de entrada: n: ordem da matriz A; A é uma matriz quadrada de 
    ordem n e b é o vetor constante.
    Saída: vetor x
    '''
    ## Calcula L e U
    #(L,U) = ...
    
    ## Calcula o vetor y, usando substituições sucessivas
    #y = 
    
    ## Calcula o vetor x, usando substituições retroativas
    #x =
    
    #return x

if __name__ == "__main__":
    
    def teste01():
        n1 = 3
        A1 = [[1, -3, 2],
              [-2, 8, -1],
              [4, -6, 5]]
        (L,U) = lu(n1, A1)
        if L != [[1, 0, 0],[-2, 1, 0],[4,3,1]]:
            print("A função retornou um resultado não esperado. ")
            print("A matriz L está diferente do que deveria ser.")
            print(L)
            result = False
        elif U != [[1,-3,2],[0,2,3],[0,0,-12]]:
            print("A função retornou um resultado não esperado. ")
            print("A matriz U está diferente do que deveria ser.")
            print(U)
            result = False
        else:
            print("Teste 1 bem sucedido")
            result = True
        return result
            
    def teste02():
        n1 = 3
        A1 = [[1, -3, 2],
              [-2, 8, -1],
              [4, -6, 5]]
        b1 = [11, -15, 29]
        x = resolve_lu(n1, A1, b1)
        if x != [2, -1, 3]:
            print("A função retornou um resultado não esperado. ")
            print("A solução deveria ser %s e o que foi retornado foi %s."%([2, -1, 3],x))
        else:
            print("Teste 2 bem sucedido")
            
    print("Testando a decomposição LU")
    ok = teste01()
#     if ok:
#         print("Testando a solução de sistema linear via LU")
#         teste02()