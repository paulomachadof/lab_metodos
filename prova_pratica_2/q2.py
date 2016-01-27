# coding: utf-8          

import sys
sys.path.append("../")

from integracao.trapz import trapz
from integracao.simpson import simpson13
    
print("2.Questão item a)")

def questao2a():
    x = [0,16]    
    y = [80,72]
    m = 1
    a1 = trapz(x, y, m)
    x = [16,32]      
    y = [72,71]
    m = 1
    a2 = trapz(x, y, m)
    x = [32,48]   
    y = [71,61]
    m = 1
    a3 = trapz(x, y, m)
    x = [48,64] 
    y = [61,53]
    m = 1
    a4 = trapz(x, y, m)
    x = [64,80]  
    y = [53,63]
    m = 1
    a5 = trapz(x, y, m)
    x = [80,96] 
    y = [63,67]
    m = 1
    a6 = trapz(x, y, m)
    x = [96,120]  
    y = [67,70]
    m = 1
    a7 = trapz(x, y, m)
    x = [120,150]  
    y = [70,72]
    m = 1
    a8 = trapz(x, y, m)
    x = [150,180] 
    y = [72,80]
    m = 1
    a9 = trapz(x, y, m)
    total = a1+a2+a3+a4+a5+a6+a7+a8+a9
    print(total)
questao2a()
#Somando todos os valores temos que area total é 12350

print("2.Questão item b) ")

def questao2b():
    x = [0,16,32,48,64,80,96]    
    y = [80,72,71,61,53,63,67]
    m = 6
    p = simpson13(x, y, m) 
    z = [96,120]
    o = [67,70]
    e = trapz(z,o, m = 1)
    a = [120,150,180]
    b = [70,72,80]
    r = simpson13(a, b, m=2)
    area = p + e + r
    print(area)
questao2b()
#Area do Terreno mais precisa: 12312