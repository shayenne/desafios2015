#!/usr/bin/env python

from array import array

# entrada
n = int(raw_input())
cod = int(raw_input())

numero = []

for i in range(n):
    numero.append(cod % 10)
    cod = cod/10;

numero.reverse()

# encontra clusters
i = 0 
clusters = []
nclusters = 0
tam_max = 1

while i < n:
    tam_atual = 1
    inicio = i
    digito = numero[i]
    i = (i+1)%n
    while numero[i] == digito and i != inicio:
        tam_atual += 1
        i = (i+1)%n
    if tam_atual > tam_max:
        tam_max = tam_atual
        clusters = []
        clusters.append([digito, inicio, (i-1)%n])
        nclusters = 1
    else:
        if tam_atual == tam_max:
            clusters.append([digito, inicio, (i-1)%n])
            nclusters +=1
    if inicio+tam_atual >= n:
        i = n


# encontra os clusters principais        

minimum = 10
digito = 10
compare = []

for cluster in clusters:
    val = (10 - cluster[0] + numero[(cluster[2] + 1)%n]) % 10
    if val < minimum:
        compare = []
        minimum = val
        compare.append(cluster)
        digito = cluster[0]
    else: 
        if val == minimum:        
            compare.append(cluster)
            digito = cluster[0]


# funcao transformacao
def transforma(ind, a = [], *args):
    tmp = []
    for i in range(n):
        tmp.append(a[(ind+i)%n])
    return int("".join(str(x) for x in tmp)), tmp
    

# transforma o numero na representacao menor
outro = list(numero)
novo = [int("".join(str(x) for x in numero)),numero]
x = 0
while x < len(compare):
    for i in range(n):
        outro[i] = (numero[i] + 10 - compare[x][0]) % 10
    tmp = []
    y = 0
    while y < len(compare):
        if compare[y][0] == compare[x][0]:
            tmp = transforma(compare[y][1], outro)
            if tmp[0] < novo[0]:
                novo = tmp
                y+=1
            elif compare[y] != compare[x]:
                compare.remove(compare[y])
            else:
                y+=1
        else:
            y+=1
    compare.remove(compare[x])

# resultado    
print "".join(str(x) for x in novo[1])

