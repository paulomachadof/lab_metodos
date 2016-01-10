# coding: utf-8

import sys
sys.path.append("../")
from sist_linear.gauss_jordan import gauss_jordan

n = 3
A =[[15, -3, -1],
    [-3, 18, -6],
    [-4, -3, 12]]
b = [3800,1200,2350]
print("7.Questão por Gauss-Jordan")
x = gauss_jordan(n, A, b)
print("x = %s"%x)

'''
Resultado obtido => x = [326.2458471760798, 242.80177187153936, 365.2823920265781]
'''