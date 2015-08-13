#!/usr/bin/env python

k = int(raw_input())

lista = map(int, raw_input().split())

lista.sort()

num = 0
for i in range(int(k/2) + 1):
    num += int(lista[i]/2) + 1

print num
