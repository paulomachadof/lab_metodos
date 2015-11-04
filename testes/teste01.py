# coding: utf-8
'''
Arquivo para testar e comparar o método da Bisseção e da Posição Falsa.
Você deve criar uma função para cada teste e chamá-la ao final do arquivo. 
Observe o exemplo dado.

'''
## Inicialmente precisamos dizer ao python para considerar o diretório acima como
## parte do caminho para as bibliotecas
import sys
sys.path.append("../")
from math import exp, cos

## Depois importamos os métodos a partir dos arquivos onde eles estão 
## definidos. Fazemos isso através do comando 
## from <arquivo_sem_a_extensão> import <nome_função>

from raiz.bisect import bissecao
from raiz.false_pos import false_pos

## definindo o teste da questão 1
def q1():
    #definindo a função que só é visível dentro de q1
    def f(x):
        return x**3-9*x+3
    a = 0
    b = 1
    epsilon = 0.001
    print("\n========================================================================")
    print("Questão 1: f(x)= x^3-9x+3, a=%s, b=%s e epsilon=%s."%(a,b,epsilon))
    print("Método da Bisseção")
    (houveErro1, raiz1) = bissecao(f,a,b,epsilon)
    if houveErro1:
        print("O Método da Bisseção retornou um erro.")
    if raiz1 is not None:
        print("Raiz encontrada: %s"%raiz1)
    print("Método da Posição Falsa")
    (houveErro2, raiz2) = false_pos(f,a,b,epsilon)
    if houveErro2:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz2 is not None:
        print("Raiz encontrada: %s"%raiz2)
    print("=========================================================================\n")
    ## Os resultados encontrados foram:
    ## Bisseção: 10 iterações, raiz: 0.3374023437
    ## Posição Falsa: 3 iterações, raiz: 0.33763504551140067
       
## defina aqui o teste da questão 2
def q2_1():
    def f(x):
        return 2**x - 3* x
    a = 0
    b = 1
    epsilon = 0.00001
    print("\n========================================================================")
    print("Questão 2: f(x)= 2^x - 3 * x , a=%s, b=%s e epsilon=%s."%(a,b,epsilon))
    print("Método da Bisseção")
    (houveErro1, raiz1) = bissecao(f,a,b,epsilon)
    if houveErro1:
        print("O Método da Bisseção retornou um erro.")
    if raiz1 is not None:
        print("Raiz encontrada: %s"%raiz1)
    print("Método da Posição Falsa")
    (houveErro2, raiz2) = false_pos(f,a,b,epsilon)
    if houveErro2:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz2 is not None:
        print("Raiz encontrada: %s"%raiz2)
    print("=========================================================================\n")
    ## Os resultados encontrados foram:
    ## Bisseção: 17 iterações, raiz: 0.4578208923339844
    ## Posição Falsa: 5 iterações, raiz: 0.4578230230476548

def q2_2():
    def f(x):
        return 2**x - 3*x
    a = 3
    b = 4
    epsilon = 0.00001
    print("\n========================================================================")
    print("Questão 2: f(x)= 2^x - 3 * x , a=%s, b=%s e epsilon=%s."%(a,b,epsilon))
    print("Método da Bisseção")
    (houveErro1, raiz1) = bissecao(f,a,b,epsilon)
    if houveErro1:
        print("O Método da Bisseção retornou um erro.")
    if raiz1 is not None:
        print("Raiz encontrada: %s"%raiz1)
    print("Método da Posição Falsa")
    (houveErro2, raiz2) = false_pos(f,a,b,epsilon)
    if houveErro2:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz2 is not None:
        print("Raiz encontrada: %s"%raiz2)
    print("=========================================================================\n")
    ## Os resultados encontrados foram:
    ## Bisseção: 17 iterações, raiz: 3.3131752014160156
    ## Posição Falsa: 11 iterações, raiz: 3.313176445658944

def q3_1():
    def f(x):
        return  4*cos(x) - exp(2*x)
    a = -5
    b = -4
    epsilon = 0.00001
    print("\n========================================================================")
    print("Questão 3: f(x)= 4*cos(x) - e(2x) , a=%s, b=%s e epsilon=%s."%(a,b,epsilon))
    print("Método da Bisseção")
    (houveErro1, raiz1) = bissecao(f,a,b,epsilon)
    if houveErro1:
        print("O Método da Bisseção retornou um erro.")
    if raiz1 is not None:
        print("Raiz encontrada: %s"%raiz1)
    print("Método da Posição Falsa")
    (houveErro2, raiz2) = false_pos(f,a,b,epsilon)
    if houveErro2:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz2 is not None:
        print("Raiz encontrada: %s"%raiz2)
    print("=========================================================================\n")
    ## Os resultados encontrados foram:
    ## Bisseção: 17 iterações, raiz: -4.712406158447266
    ## Posição Falsa: 3 iterações, raiz: -4.712409147263011

def q3_2():
    def f(x):
        return  4*cos(x) - exp(2*x)
    a = -2
    b = -1
    epsilon = 0.00001
    print("\n========================================================================")
    print("Questão 3: f(x)= 4*cos(x) - e(2x) , a=%s, b=%s e epsilon=%s."%(a,b,epsilon))
    print("Método da Bisseção")
    (houveErro1, raiz1) = bissecao(f,a,b,epsilon)
    if houveErro1:
        print("O Método da Bisseção retornou um erro.")
    if raiz1 is not None:
        print("Raiz encontrada: %s"%raiz1)
    print("Método da Posição Falsa")
    (houveErro2, raiz2) = false_pos(f,a,b,epsilon)
    if houveErro2:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz2 is not None:
        print("Raiz encontrada: %s"%raiz2)
    print("=========================================================================\n")
    ## Os resultados encontrados foram:
    ## Bisseção: 17 iterações, raiz: -1.5597496032714844
    ## Posição Falsa: 3 iterações, raiz: -1.5597511942763267

def q3_3():
    def f(x):
        return  4*cos(x) - exp(2*x)
    a = 0
    b = 1
    epsilon = 0.00001
    print("\n========================================================================")
    print("Questão 3: f(x)= 4*cos(x) - e(2x) , a=%s, b=%s e epsilon=%s."%(a,b,epsilon))
    print("Método da Bisseção")
    (houveErro1, raiz1) = bissecao(f,a,b,epsilon)
    if houveErro1:
        print("O Método da Bisseção retornou um erro.")
    if raiz1 is not None:
        print("Raiz encontrada: %s"%raiz1)
    print("Método da Posição Falsa")
    (houveErro2, raiz2) = false_pos(f,a,b,epsilon)
    if houveErro2:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz2 is not None:
        print("Raiz encontrada: %s"%raiz2)
    print("=========================================================================\n")
    ## Os resultados encontrados foram:
    ## Bisseção: 17 iterações, raiz: 0.5978889465332031
    ## Posição Falsa: 12 iterações, raiz: 0.5978851851704279

## chamando os testes
#q1()
#q2_1()
#q2_2()
q3_1()
q3_2()
q3_3()
