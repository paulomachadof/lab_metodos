# coding: utf-8
'''
Created on Aug 25, 2015

@author: emanuele
'''

def false_pos(f, a, b, epsilon, maxIter = 50,mostraTabela = False):
    """Executa o método da Posição Falsa para achar o zero de f no intervalo 
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz,k), onde houveErro é booleano.
    """
    ## Inicializar as variáveis fa e fb
    fa = f(a)
    fb = f(b)
    
    ## Teste para saber se a função muda de sinal. Se não mudar, mostrar
    ## mensagem de erro
    if fa*fb > 0:
        ## Mostrar mensagem
        print("ERRO: Função não mudou de sinal no intervalo dado")
        return (True, None,k)
    ## Inicializa tamanho do intervalo intervX usando a função abs
    intervX = abs(b-a)
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    if intervX <= epsilon:
        return (False, (a+b)/2,k)
    ## Teste se raiz está nos extremos dos intervalos
    if abs(fa) <= epsilon:
        return (False,a,k)
    if abs(fb) <= epsilon:
        return (False,b,k) 
    
    if mostraTabela:
        ## Mostra na tela cabeçalho da tabela
        print("k\t  a\t\t  fa\t\t  b\t\t  fb\t\t  x\t\t  fx\t\tintervX")
    
    for k in range(1, maxIter+1):
        ## Calcula x, fx
        x = (a * fb - b * fa)/(fb - fa)
        fx= f(x)
        
        if mostraTabela:
            ## Mostra valores na tela
            print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k,a, fa, b, fb, x, fx, intervX))

        ## Teste do critério de parada módulo da função
        if abs(fx) <= epsilon:
            return (False,x,k)
        
        ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        ## as variáveis apropriadamente
        
        if fa * fx > 0:
            a = x 
            fa = fx
        else:
            b = x
            fb = fx
        
        ## Atualiza intervX e checa o outro critério de parada
        intervX = abs(b-a)
        if intervX <= epsilon:
            return(False, (a+b)/2,k)
       
    ## Se chegar aqui é porque o número máximo de iterações foi atingido
    print("O Número máximo de interações foi atingido")
    return (True, x,k)
    

if __name__ == "__main__":
    
    def f1(x):
        return x**3-9*x+3
    a = 0
    b = 1
    epsilon = 0.001
    maxIter = 20
    print("Método da Posição Falsa")
    (houveErro, raiz,k) = false_pos(f1,a,b,epsilon,maxIter,mostraTabela=False)
    if houveErro:
        print("O Método da Posição Falsa retornou um erro.")
    if raiz is not None:
        print("Raiz encontrada: %s"%raiz)
                
