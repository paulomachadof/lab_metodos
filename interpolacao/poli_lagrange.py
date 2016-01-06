# coding: utf-8

## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from interpolacao.poli_aval import poli_aval

def interpola_lagrange(x, y, n):
    """
    Interpola os valores nos vetores x e y usando um polinômio de grau n 
    calculado através da forma de Lagrange
    """
    
    ## A primeira coisa a fazer é checar que o número de elementos em x e y é
    ## igual a n+1. Se forem diferentes, saia da função retornando None.
    
    if len(x) != n+1 or len(y) != n+1:
        return None
    
    a = (n+1) * [0]
    for k in range(0, n+1):
        den = 1
        num = [1]
        for j in range(0,n+1):
            if j != k:
                den = den *(x[k] - x[j]) 
                num.insert(0, 0)
                for i in range(0,len(num)-1):
                    num[i] = num[i] - num[i+1] * x[j]
        for i in range(0,len(num)):
            num[i] = y[k] * num[i]/den 
            a[i] = a[i] + num[i] 
    return a
    ##retorne o vetor solução
    
if __name__ == "__main__":
    ## Teste a função interpola_gauss para interpolação linear
    def teste_interp_linear():
        x = [0.1, 0.6]
        y = [1.221, 3.32]
        n = 1
        p = interpola_lagrange(x,y,n)
        v = poli_aval(p,0.2)
        print(v)
       
    def teste_interp_quadratica():
        x = [-1, 0, 2]
        y = [4, 1, -1]
        n = 2 
        p = interpola_lagrange(x,y,n)
        v = poli_aval(p, 1)
        print(v) 
        
teste_interp_linear()
teste_interp_quadratica()