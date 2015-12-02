def gauss_jordan(n, A, b):
    '''
    Executa o método de Gauss-Jordan para resolver o sistema linear Ax=b 
    transformando a matriz A na matriz identidade.
    Parâmetros de entrada: n: ordem da matriz A; A é uma matriz quadrada de ordem n e b é o vetor constante.
    Saída: vetor solução x
    '''
    
    for k in range(0,n):
        for j in range(k+1, n):
            A[k][j] = A[k][j] / A[k][k]
        b[k] = b[k] / A[k][k]
        A[k][k] = 1    
        
        for i in range(0,n):
            if i != k:
                m = -A[i][k] / A[k][k]
                A[i][k] = 0 
                for j in range(k+1,n):
                    A[i][j] = m * A[k][j] + A[i][j]
                b[i] = m * b[k] + b[i]

    return b

if __name__ == "__main__":

    def teste01():
        n1 = 3
        A1 = [[1, -3, 2],
              [-2, 8, -1],
              [4, -6, 5]]
        b1 = [11, -15, 29]
        x = gauss_jordan(n1, A1, b1)
        if x != [2, -1, 3]:
            print("A função retornou um resultado não esperado. ")
            print("A solução deveria ser %s e o que foi retornado foi %s."%([2, -1, 3],x))
        else:
            print("Teste 1 bem sucedido")

    print("Testando o método de gauss-jordan")
    teste01()