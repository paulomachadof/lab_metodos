# coding: utf-8

def poli_aval(a, x):
    """
    Calcula o valor de p(x), onde p é um polinômio definido pelos coeficientes
    no vetor a e x é o valor a ser aplicado.
    
    """
    n = len(a) - 1
    b = a[n]
    for i in range(n-1,0,-1):
        b = b*x+a[i]
    b = b*x+a[0]
    return b
if __name__ == "__main__":
    p = [3, 5, -3, 1]
    x = 2
    v = poli_aval(p,x)
    print(v)