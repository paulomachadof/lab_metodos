import sys
sys.path.append("../")

from sist_linear.lu import identidade

def inversa(n, A):
  
    I=identidade(n)
    
    for k in range(0, n):
        for j in range(k+1, n):
            A[k][j] = A[k][j]/A[k][k]
        for j in range(0,n):
            I[k][j] = I[k][j]/A[k][k]
        A[k][k] = 1    
        for i in range(0, n):
            if i != k:
                m=-A[i][k]/A[k][k]
                A[i][k]=0
                for j in range(k+1,n):
                    A[i][j]=m * A[k][j]+ A[i][j]
                for j in range(0,n):
                    I[i][j]=m * I[k][j] + I[i][j]
    
    return I

if __name__ == "__main__":
    
    def questao7():
        n = 3
        A =[[15, -3, -1],
           [-3, 18, -6],
           [-4, -3, 12]]
        x = inversa(n, A)
        print("7. Questão item b)")
        print("Matriz Inversa: %s"%x)
    
    questao7()