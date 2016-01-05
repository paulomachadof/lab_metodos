# coding: utf-8

## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

from sist_linear.gauss import gauss
from sist_linear.lu import identidade
from interpolacao.poli_aval import poli_aval

def interpola_gauss(x, y, n):
    """
    Interpola os valores nos vetores x e y usando um polinômio de grau n 
    calculado através da resolução de sistema linear pelo método da eliminação
    de gauss.
    Retorna a lista de coeficientes do polinômio
    """
    
    ## A primeira coisa a fazer é checar que o número de elementos em x e y é
    ## igual a n+1. Se forem diferentes, saia da função retornando None.
    
    #if len(x) != n+1 or len(y)...
    
    ## Inicialize a matriz de Vandermonde, inicializando a matriz a partir de 
    ## uma matriz identidade.
    
    A = identidade(n+1)
    
    ## Você precisará de dois loops encadeados, um para percorrer as colunas e
    ## outro para percorrer os elementos de x (linhas) e popular a matriz A
    
    
    ## Chame o método de Gauss, lembrando que a ordem da matriz é n+1
    #x = gauss(...)
    
    ##retorne o vetor solução
    

if __name__ == "__main__":
    ## Teste a função interpola_gauss para interpolação linear
    def teste_interp_linear():
        #x = [...]
        #y = [...]
        #n = ...
        #p = interpola_gauss(...)
        #v = poli_aval(...)
        #print(v)
       
    def teste_interp_quadratica():
        #x = [...]
        #y = [...]
        #n = ...
        #p = interpola_gauss(...)
        #v = poli_aval(...)
        #print(v) 
    teste_interp_linear()
    teste_interp_quadratica()