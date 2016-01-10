# coding: utf-8

import sys
sys.path.append("../")
from sist_linear.seidel import seidel

if __name__ == "__main__":
    n = 3
    A =[[5, 3, 1],
        [5, 6, 1],
        [1, 6, 7]]
    b = [1,2,3]
    epsilon = 0.000001
    print("5.Questão Resolvendo por Gauss-Seidel ")
    x = seidel(n,A,b,epsilon)
    print("x = %s"%x)
    
'''
Resultado:
x = [-0.02941147571366523, 0.3333330154418945, 0.14705905472318542] 
'''