#!/usr/bin/env python

n = int(raw_input())

paint = []
for i in range(n):
    x = raw_input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    paint.append(x)

print paint

faixas = [[0, 1000000000]]

numfaixas = 1

for i in range(n):
    ant = 0
    while faixas[ant][1] < paint[i][0]:
        ant += 1
    pos = ant
    while faixas[pos][0] > paint[i][1]:
        pos += 1

    if ant == pos:
        if paint[i][2] != faixas[ant][2]:
            faixas.insert(ant+1, [paint[i][1], faixas[ant][1], faixas[ant][2]])
            faixas.insert(ant+1, paint[i])
            faixas[ant][1] = paint[i][0]
    else:
        if paint[i][2] == faixas[ant][2]:
            faixas[ant][1] = paint[i][1]
            

