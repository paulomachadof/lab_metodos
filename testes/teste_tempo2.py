# coding: utf-8

'''
Arquivo para medir e comparar o tempo de excução de um trecho de código.
É exigida a versão 3.3 do Python ou superior para o código funcionar
'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")

import time

## Depois importamos os métodos a partir dos arquivos onde eles estão 
## definidos. Fazemos isso através do comando 
## from <arquivo_sem_a_extensão> import <nome_função>
from raiz.newton import newton
from raiz.newton_poli import newton_poli

# definindo a função do polinômio e a sua derivada
def p(x):
    return -3*x**6 + 2*x**5 - 5*x**4 + 6*x**3 + 7*x**2 - 4*x+3
def plin(x):
    return -18*x**5 + 10*x**4 - 20*x**3 + 18*x**2 + 14*x - 4	 

#definindo os coeficientes do polinômio
n = 6
a = [3,-4,7,6,-5,2,-3]
epsilon = 0.000000000001 
maxIter = 100	
x = 1.1
print("p(x) = -3x^6 + 2x^5-5x^4+6x^3+7x^2-4x+3")
tni = time.perf_counter()
(houveErro1, raiz1) = newton(p,plin,x,epsilon, maxIter)
tnf = time.perf_counter()
print("Tempo de execução do Método de Newton-Raphson: %s ms"%((tnf-tni)*1000))
if not houveErro1:
    print("Raiz encontrada: %s"%raiz1)
else:
    print("O método de Newton-Raphson retornou um erro")
print("\n\n")
tnpi = time.perf_counter()
(houveErro2, raiz2) = newton_poli(n,a,x,epsilon, maxIter)
tnpf = time.perf_counter()
print("Tempo de execução do Método de Newton-Raphson para Polinômios: %s ms"%((tnpf-tnpi)*1000))
if not houveErro2:
    print("Raiz encontrada: %s"%raiz2)
else:
    print("O Método de Newton-Raphson para polinômios retornou um erro.")

