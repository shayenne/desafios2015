#!/usr/bin/env python

n = int(raw_input())

cidades = {'first':0}
dados = []
dia = 0

for i in range(n):
    dados.append(raw_input().split())
    dados[i][2] = int(dados[i][2])
    if cidades.has_key(dados[i][1]):
        cidades[dados[i][1]] += dados[i][2]
    else:
        cidades[dados[i][1]] = dados[i][2]
    if cidades[dados[i][1]] > cidades['first']:
        cidades['first'] = dados[i][1]

fortunes = {}
fortunes[cidades['first']] = 1

m, k = map(int, raw_input().split())

viagens = []
for j in range(k):
    viagens.append(raw_input().split())

print n
print dados
print m, k
print viagens
print cidades
print fortunes
