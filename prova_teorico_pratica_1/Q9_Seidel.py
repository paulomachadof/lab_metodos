# coding: utf-8

import sys
sys.path.append("../")
from sist_linear.seidel import seidel
from sist_linear.gauss_jordan import gauss_jordan

'''
Resolvendo os sistemas por por Gauss-Seidel.
'''
if __name__ == "__main__":
    
    def conj1():
        n = 3
        A =[[9,3,1],
            [-6,8,0],
            [2,5,-1]]
        b = [13,2,6]
        print("9.Questão por Gauss-Seidel\n") 
        print("Conjunto 1")
        epsilon = 0.001
        x = seidel(n, A, b, epsilon, iterMax=50)
        print("x = %s"%x) 
        
    def conj2():
        n = 3
        A =[[1,1,6],
            [1,5,-1],
            [4,2,-2]]
        b = [8,5,4]
        print("Conjunto 2")
        epsilon = 0.5
        x = seidel(n, A, b, epsilon, iterMax=50)
        print("x = %s"%x) 
         
    def conj3():
        n = 3
        A =[[-3,4,5],
            [-2,2,-3],
            [0,2,-1]]
        b = [6,-3,1]
        print("Conjunto 3")
        epsilon = 0.5
        x = seidel(n, A, b, epsilon, iterMax=50)
        print("x = %s"%x) 
            
conj1()
conj2()
conj3()

'''
O Método não converge.
'''