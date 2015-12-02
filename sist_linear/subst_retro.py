'''
Created on Dec 1, 2015

@author: emanuele
'''

def substituicoes_retroativas(n, A, b):
    '''Executa o método das substituições retroativas para resolver o sistema 
       linear triangular superior Ax=b.
       Parâmetros de entrada: n: ordem da matriz A; A é uma matriz triangular
       superior e b é o vetor constante. 
    '''
    x = n * [0]   
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma)/A[i][i]
    
    return x

if __name__ == "__main__":
    
    def teste01():
        n1 = 4
        A1 = [[5, -2, 6, 1],
             [0, 3, 7, -4],
             [0, 0, 4, 5],
             [0, 0, 0, 2]]
        b1 = [1, -2, 28, 8]
        x = substituicoes_retroativas(n1, A1, b1)
        if x != [-3, 0, 2, 4]:
            print("A função retornou um resultado não esperado. ")
            print("A solução deveria ser %s e o que foi retornado foi %s."%([-3,0,2,4],x))
        else:
            print("Teste 1 bem sucedido")
            
    print("Testando o método das substituições retroativas")
    teste01()
