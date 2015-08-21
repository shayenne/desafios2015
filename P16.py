# Shayenne Moura
#!/usr/bin/env python

import math

k = int(raw_input())
lista = []

for i in range(k):
    x = int(raw_input())
    lista.append(x)

                 
def eh_primo(k):
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

                 
def encontra_primo(n, tabela):
    try:
        tabela[n-1]
        return tabela
    except IndexError:
        j = tabela[len(tabela) - 1]
        i = len(tabela)
        while i < n:
            j+=1
            if eh_primo(j):
                i+=1
                tabela.append(j)
                
        return tabela
    
tabela = [2]
for i in range(len(lista)):
    encontra_primo(lista[i], tabela)
    print tabela[lista[i]-1]
