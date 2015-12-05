'''
Created on 27/11/2015

@author: paulomachado
'''
import sys
sys.path.append("../")

from raiz.newton_poli import newton_poli   

'''
Comando para plotar gráfico no Octave:
ezplot("5*x^5 - 2*x^4 + 3*x^2 - 8*x - 10",[-1.5,2]);
Com isso, temos que um bom valor para x0 é 1.4.
'''

def acha_raiz():
    n = 5
    a = [-10, -8, 3, 0, -2, 5]
    x0 = 1.4
    epsilon = 0.00001
    print("Q3. Encontrando a raiz de f(x) = 5x^5 - 2x^4 + 3x^2 - 8x - 10 = 0 através do Método de Newton Para Polinômios")
    (houveErro, raiz) = newton_poli(n,a,x0,epsilon)
    if houveErro:
        print("O Método de Newton Para Polinômios a retornou um erro.")
    if raiz is not None:	
        print("\nRaiz encontrada: %s"%raiz)
        
acha_raiz()
    
'''
Raiz Encontrada: 1.3429105189708204
Iterações: 3
'''
