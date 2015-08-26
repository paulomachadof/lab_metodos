# coding: utf-8
'''
Created on Aug 25, 2015

@author: emanuele
'''

def false_pos(f, a, b, epsilon, maxIter = 50):
    """Executa o método da Posição Falsa para achar o zero de f no intervalo 
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    ## Inicializar as variáveis fa e fb
    # fa = ...
    # fb = ...
    
    ## Teste para saber se a função muda de sinal. Se não mudar, mostrar
    ## mensagem de erro
    if fa*fb > 0:
        ## Mostrar mensagem
        # print("")
        return (True, None)
    ## Inicializa tamanho do intervalo intervX usando a função abs
    # intervX = ...
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    # if intervX ...:
    
    ## Teste se raiz está nos extremos dos intervalos
    # if ..
    
    # if...
    
    ## Iniciliza o k, dessa vez usaremos um for
    for k in range(0, maxIter+1):
        ## Calcula x, fx
        # x = ...
        # fx = ...
        
        ## Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k,a, fa, b, fb, x, fx, intervX))
        
        ## Teste do critério de parada módulo da função
        
        
        ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        ## as variáveis apropriadamente
        
        # if fa * fx ...
        #     a = ...
        #     fa = ...
        # else:
        #     b = ...
        #     fb = ...
        
        ## Atualiza intervX e checa o outro critério de parada
        # intervX = ...
       
    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    # print("")
    return (True, x)
    

if __name__ == "__main__":
    
    def f1(x):
        return x**3-9*x+3
    a = 0
    b = 1
    epsilon = 0.001
    maxIter = 20
    print("Método da Posição Falsa")
    (houveErro, raiz) = false_pos(f1,a,b,epsilon,maxIter)
    if houveErro:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz is not None:
        print("Raiz encontrada: %s"%raiz)
                
