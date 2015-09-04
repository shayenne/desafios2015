# Shayenne Moura
#!/usr/bin/env python
import sys
import math
n = int(raw_input())

if n % 2:
    exit()

def calcula_soma(y):
    total = 0
    while y > 0:
        total += y % 10
        y = int(y / 10)

    return total

soma = [0]*((n*9/2)+1)
for i in range(int(math.pow(10, n/2))):
    x = calcula_soma(i)
    soma[x] += 1
        
print int(sum([math.pow(x, 2) for x in soma]))
        
