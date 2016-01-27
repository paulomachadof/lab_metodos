# coding: utf-8

def popula_vetores(f, a, b, m ):
    """
    Cria dois vetores x e y a partir dos valores de f, a, b e m. 
    f é a função a ser aplicada
    a e b são os limites do intervalo
    m é o número de subintervalos.
    Retorna tupla (x,y)
    
    """
    x = (m+1)*[0]
    y = (m+1)*[0]
    # escreva o seu código aqui
    
    return (x,y)
    
if __name__ == "__main__":
    from math import log
    def f(x):
        return x**3 * log(x)
    a = 1
    b = 3
    m = 4
    (x,y) = popula_vetores(f, a, b, m)
    print("Valores populados:")
    print("i\txi\tf(xi)")
    for i in range(0,m+1):
        print("%d\t%.4f\t%s"%(i,x[i],y[i]))
    
        