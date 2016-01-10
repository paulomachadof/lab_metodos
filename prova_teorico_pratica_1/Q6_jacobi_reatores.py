# coding: utf-8

import sys
sys.path.append("../")
from sist_linear.jacobi import jacobi

'''
O sistema linear é montado a partir das equações de liquibrio de massa de cada reator,
resolvemos o sistema pelo método de Gauss-Jacobi para encontrar as incógnitas (c), concentração.
'''

n = 5
A =[[-9, 0, 3, 0, 0],
[4, -4, 0, 0, 0],
[0, 2, -9, 0, 0],           
[0, 1, 6, -9, 2],    
[5, 1, 0, 0, -6]]
b = [-120, 0, -350, 0, 0]

epsilon = 0.05
print("Resovlendo 6.Questão por Gauss-Jacobi")
x = jacobi(n,A,b,epsilon)
print("x = %s"%x)

'''
Resultado:
x = [28.244170096021946, 28.244170096021946, 44.951989026063096, 38.879743941472334, 28.084133516232
'''