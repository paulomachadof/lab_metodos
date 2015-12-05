# coding: utf-8
# Comando para plotar gŕafico no Octave: ezplot("x*(cosh(50/(2*x))-1)-0.80",[390,392]);

'''
Created on 28/11/2015 

@author: paulomachado
'''
import sys
sys.path.append("../")

from raiz.bisect import bissecao
from raiz.false_pos import false_pos
from math import cosh,sinh

def l_bissecao(x):
    return x * (cosh(50/(2*x)) - 1) - 0.80

a = 390
b = 392
epsilon = 0.00000001
maxIter = 50

print("Q1. Determinando o Comprimento de L através dos Métodos: \n")
print("Método da Bisseção")
(houveErro, raiz,k) = bissecao(l_bissecao,a,b,epsilon,maxIter,mostraTabela = True)
if houveErro:
    print("O Método da Bisseção retornou um erro.")
if raiz is not None:
    print("Raiz encontrada: %s"%raiz)
L = 2 * raiz*sinh(50/(2*raiz))
print("Valor de L: %s"%L) 
#print("O número de iterações: %s"%k)
''' 

Raiz da Equação: 390.75826058909297
Interações: 28
E o Valor de L encontrado foi: 50.034117037925476

'''

def l_false_pos(x):
    return x * (cosh(50/(2*x)) - 1) - 0.80

print("\nMétodo da Posição Falsa")
(houveErro, raiz,k) = false_pos(l_false_pos, a, b, epsilon, maxIter,mostraTabela=True)
if houveErro == False:
    print("Raiz encontrada %s"%raiz)
else:
    print("O método da posição falsa retornou um erro.")
L = 2 * raiz*sinh(50/(2*raiz))
print("Valor de L: %s"%L) 
#print("O número de iterações: %s"%k)

''' 
Raiz da Equação: 390.7582652735814
Interações: 2
E o Valor de L encontrado foi: 50.03411703710731

d) O Método  da Posição Falsa funcinou melhor porque 
encontrou a raiz com menos iterações no mesmo intervalo dado.
Ao invés de selecionar o ponto médio de cada intervalo, o método
da posição falsa usa o ponto onde a reta secante intersecta o eixo
das abscissas. Como o intervalo é pequeno e próximo da raiz da função,
o método convergiu rapidamente.
'''
