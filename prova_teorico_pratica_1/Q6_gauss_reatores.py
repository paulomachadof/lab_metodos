# coding: utf-8

'''
O sistema linear é montado a partir das equações de liquibrio de massa de cada reator,
resolvemos o sistema pelo método de Gauss para encontrar as incógnitas (c), concentração.
'''

import sys
sys.path.append("../")
from sist_linear.gauss import gauss

n = 5
A =[[-9, 0, 3, 0, 0],
    [4, -4, 0, 0, 0],
    [0, 2, -9, 0, 0],           
    [0, 1, 6, -9, 2],    
    [5, 1, 0, 0, -6]]
b = [-120, 0, -350, 0, 0]
print("Resolvendo 6.Questão por Gauss")
x = gauss(n, A, b)
print("x = %s"%x)

'''
Resultado:
x = [28.4, 28.4, 45.199999999999996, 39.599999999999994, 28.400000000000002]
'''