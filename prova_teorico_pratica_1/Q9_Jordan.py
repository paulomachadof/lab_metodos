# coding: utf-8
'''
Created on Dec 1, 2015

@author: emanuele
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")
from sist_linear.gauss_jordan import gauss_jordan

if __name__ == "__main__":
    
    def conj1():
        n = 3
        A =[[9,3,1],
            [-6,8,0],
            [2,5,-1]]
        b = [13,2,6]
        print("9.Questão por Gauss-Jordan\n") 
        print("Conjunto 1")
        x = gauss_jordan(n, A, b)
        print("x = %s"%x) 
        
    def conj2():
        n = 3
        A =[[1,1,6],
            [1,5,-1],
            [4,2,-2]]
        b = [8,5,4]
        print("Conjunto 2")
        x = gauss_jordan(n, A, b)
        print("x = %s"%x) 
    
    def conj3():
        n = 3
        A =[[-3,4,5],
            [-2,2,-3],
            [0,2,-1]]
        b = [6,-3,1]
        print("Conjunto 3")
        x = gauss_jordan(n, A, b)
        print("x = %s"%x) 
            
conj1()
conj2()
conj3()