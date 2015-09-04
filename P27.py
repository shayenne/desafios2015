#!/usr/bin/env python

def busca_binaria(x, v):
    print v
    e = 0
    d = len(v)-1
    while e <= d:
        m = int((e+d)/2)
        if x >= v[m][0] and x < v[m][1]:
            return m
        if x >= v[m][1]:
            e = m + 1
        else:
            d = m - 1
    print "Erro ini"

n = int(raw_input())

cnt = 0
intervalo = [[0, 32000]]
grau = [0]*n

x, y = map(int, raw_input().split())
print x, y
for i in range(n):
    lin = y
    
    while lin == y:
        new = busca_binaria(x, intervalo)
        grau[new] += 1
        
        intervalo.insert(new+1, [x, intervalo[new][1]])
        intervalo[new][1] = x

        x, y = map(int, raw_input().split())
        
    cnt += 1

print grau
