'''
Created on 27/11/2015

@author: paulomachado
'''
import sys
sys.path.append("../")

from raiz.newton import newton
from raiz.secante import secante
from math import cos, sin

def pi_newton(x):
    return cos(x) + 1
def df(x):
    return -sin(x)

x0 = 3
x1 = 3.2
epsilon = 0.000001
maxIter = 50

print("Q2. Calculando o Valor de Pi pelos Métodos: \n")
print("Método de Newton-Raphson")
(houveErro, raiz) = newton(pi_newton,df,x0,epsilon)
if houveErro == False:
    print("Valor de Pi Encontrado: %s"%raiz)
else:
    print("O método da Newton-Raphson retornou um erro.")

'''
Valor de pi encontrado utilizando o Método de Newton: 3.1404889256636337
Iterações: 7
'''
def secante_newton(x):
    return cos(x) + 1

print("\nMétodo da Secante")
(houveErro, raiz) = secante(secante_newton,x1,x0,epsilon)
if houveErro:
    print("O Método da Secante a retornou um erro.")
if raiz is not None:
    print("Valor de Pi Encontrado: %s"%raiz)

'''
Valor de Pi encontrado utilizando o Metodo da Secante: 3.142808963152471
Iterações: 12

O método de Newton-Raphson funcionou melhor, porque encontrou o valor da 
raiz em menos iterações do que o método da secante. Isso traduz em menos 
tempo de execução e menos processamento da maquina para encontrar a raiz 
da função. 
'''
