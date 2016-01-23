# coding: utf-8

## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from interpolacao.poli_aval import poli_aval

def diferenca_dividida(x,y, i, ordem):
    """
    Calcula o operador de diferença de dividida de ordem "ordem" dos elementos.
    """
    if ordem == 0:
        return y[i]

    resulta = (diferenca_dividida(x,y,i+1,ordem-1) - diferenca_dividida(x,y,i,ordem-1))/(x[i+ordem] - x[i])

    return resulta

def interpola_newton(x, y, n):
    """
    Interpola os valores nos vetores x e y usando um polinômio de grau n 
    calculado através de Newton.
    Retorna a lista de coeficientes do polinômio
    """
    
    #Testando para saber se o tamanho de x e de y é diferente de n+1
  
    if len(x) != n+1 or len(y) != n+1:
        return None
    
    
    
    a = (n+1)*[0]
    a[0] = y[0]

    
    for k in range(1,n+1):
        p = [1]
        for j in range(0,k):
            p.insert(0,0)
            for i in range(0,len(p)-1):
                p[i] = p[i] - (p[i+1]*x[j])
        difDiv = diferenca_dividida(x,y,0,k)
        for i in range(0,len(p)):
            p[i] = (p[i]*difDiv)
            a[i] = a[i] + p[i]

    return a 
    

if __name__ == "__main__":
    ## Teste interpolação linear
    def teste_diferenca_dividida():
        x = [-1, 0, 2]
        y = [4, 1, -1]
        i = 0
        ordem = 2
        z = diferenca_dividida(x,y,i,ordem)

        print(z)
    
    def teste_interp_linear():
        x = [0.1, 0.6]
        y = [1.221, 3.32]
        n = 1
        p = interpola_newton(x,y,n)
        v = poli_aval(p,0.2)
        print(v)
       
    def teste_interp_quadratica():
        x = [-1, 0, 2]
        y = [4, 1, -1]
        n = 2
        p = interpola_newton(x,y,n)
        v = poli_aval(p,1)
        print(v) 
    teste_interp_linear()
    teste_interp_quadratica()
    teste_diferenca_dividida()