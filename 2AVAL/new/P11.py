"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P11 - 1005. Stone Pile
"""
#!/usr/bin/env python

def minima_distancia(m, x, v):
    if len(v) < 1:
        return x;
    left = 0
    if x + v[0] <= m + 1:
        left = minima_distancia(m, x+v[0], v[1:len(v)])
    right = minima_distancia(m, x, v[1:len(v)])
    
    if abs(m - left) > abs(m - right):
        return right
    
    return left
    
    

n = int(raw_input())

stones = map(int, raw_input().split())

#Diminui a pilha da recursao
stones.sort()
stones.reverse()

average = sum(stones)/2.0

calculo =  minima_distancia(average, stones[0], stones[1:len(stones)])

menor = abs(int((average - calculo)*2))
if menor > 0:
    print menor
else:
    print menor*(-1)


