#/usr/bin/env python 

import math

def eh_primo(k):
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

tabela = []
count = 0
for i in range(100, 1000):
    if eh_primo(i):
        tabela.append(i)
        count +=1

n =int(raw_input())

for i in range(n-2):
    

print count
