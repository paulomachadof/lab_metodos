# coding: utf-8
'''
Created on 14 de dez de 2015

@author: emanuele
'''

def norma(n,v,x):
    """Calcula a norma entre dois vetores v e x de tamanho n.
    """
    maxnume = 0
    maxdemo = 0
    
    for i in range(0,n):
        if abs(v[i]-x[i]) > maxnume:
            maxnume = abs(v[i]-x[i])
        if abs(v[i]) > maxdemo:
            maxdemo = abs(v[i])
    
    return maxnume/maxdemo

if __name__ == "__main__":
    ## teste da função
    x0 = [0.7, -1.6, 0.6]
    x1 = [0.96, -1.86, 0.94]
    n = 3
    d = norma(n,x1,x0)
    print("Testando a norma de vetores")
    print(d)