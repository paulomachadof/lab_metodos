# coding: utf-8
'''
Created on Aug 18, 2015

@author: emanuele
'''

def bissecao(f, a, b, epsilon, maxIter = 50):
    """Executa o método da bisseção para achar o zero de f no intervalo 
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
    
    ## Mostra na tela cabeçalho da tabela
    print("k\t  a\t\t  fa\t\t  b\t\t  fb\t\t  x\t\t  fx\t\tintervX")
    
    ## Inicializa tamanho do intervalo intervX usando a função abs, x e fx
    # intervX = ...
    # x = ...
    # fx = ...
    
    ## Mostra dados de inicialização
    print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(a, fa, b, fb, x, fx, intervX))
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    # if intervX ...:
    
    ## Iniciliza o k
    # k = ...
    
    ## laço
    while k <= maxIter:
        ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        ## as variáveis apropriadamente
        
        # if fa * fx ...
        #     a = ...
        #     fa = ...
        # else:
        #     b = ...
        #     fb = ...
        
        ## Atualiza intervX, x, e fx
        
        # intervX = ...
        # x = ...
        # fx = ...
        
        ## Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k,a, fa, b, fb, x, fx, intervX))
        
        ## Teste do critério de parada
        
        # if intervX ... 
        #    return ...
        k = k+1
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
    print("Método da Bisseção")
    (houveErro, raiz) = bissecao(f1,a,b,epsilon,maxIter)
    if houveErro:
        print("O Método da Bisseção retornou um erro.")
    if raiz is not None:
        print("Raiz encontrada: %s"%raiz)
                
