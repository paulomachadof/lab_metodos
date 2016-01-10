# coding: utf-8
'''
Created on Dec 8, 2015

@author: emanuele
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")
from sist_linear.lu import lu

if __name__ == "__main__":
    
    def questao8():
        n1 = 3
        A1 = [[1, 1, 1],
              [2, 1, -1],
              [3, 2, 0]]
        (L,U) = lu(n1, A1)
        print(L)    
        print(U)
    questao8()