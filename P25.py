# Shayenne Moura
#!/usr/bin/env python

import math
"""
tabela = []
num = 1
for i in range(10):
    num *= int(raw_input())
"""
def eh_primo(k):
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True
    
lista = []
primos = {}
for i in range(2, 10000):
    if eh_primo(i):
        lista.append(i)

for i in range(10):
    n = int(raw_input())
    j = 0
    while j < len(lista) and n != 1:
        while n % lista[j] == 0:
            n /= lista[j]
            if primos.has_key(lista[j]):
                primos[lista[j]] += 1
            else:
                primos[lista[j]] = 1
        j += 1

num = 1
for p in primos.keys():
    num *= primos[p]+1

print num
print primos
print num % 10
    
    
