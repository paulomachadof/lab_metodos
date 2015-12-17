'''
Created on 21/11/2015

@author: paulomachado
'''
import sys
sys.path.append("../")
from sist_linear.jacobi import jacobi 
from sist_linear.seidel import seidel
from sist_linear.gauss import gauss

if __name__ == "__main__":
    
    def teste01():
        n = 5
        A =[[9, 0, -3, 0, 0],
        [4, -4, 0, 0, 0],
        [0, -2, 9, 0, 0],           
        [0, 1, 6, -9, 2],    
        [5, 1, 0, 0, -6]]
        b = [120, 0, 350, 0, 0]
        epsilon = 0.05    
        
        print("Resolvendo por Gauss-Seidel")
        x = seidel(n, A, b,epsilon)
        print("x = %s"%x)
        
    def teste02():
        n = 5
        A =[[9, 0, -3, 0, 0],
        [4, -4, 0, 0, 0],
        [0, -2, 9, 0, 0],           
        [0, 1, 6, -9, 2],    
        [5, 1, 0, 0, -6]]
        b = [120, 0, 350, 0, 0]
        epsilon = 0.05
        
        print("Resolvendo por Gauss-Jacobi")
        x = jacobi(n, A, b,epsilon)
        print("x = %s"%x)
        
    def teste03():
        n = 5
        A =[[9, 0, -3, 0, 0],
        [4, -4, 0, 0, 0],
        [0, -2, 9, 0, 0],           
        [0, 1, 6, -9, 2],    
        [5, 1, 0, 0, -6]]
        b = [120, 0, 350, 0, 0]
        
        print("Resolvendo por Gauss")
        x = gauss(n, A, b)
        print("x = %s"%x)
            
teste01()
teste02()
teste03()