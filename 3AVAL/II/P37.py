"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P37 - 284D. Cow Program
"""

def bfs(mais, menos):
    soma = [-1 for i in xrange(n+1)]
    v = 0

    fila = [[],[]]
    for i in xrange(len(menos)):
        print menos
        if menos[v][i] != [] and menos[v][i][2] == 0:
            fila[0].append([v, menos[i]])

    for i in xrange(len(mais)):
        print mais
        if mais[v][i][2] == 0:
            fila[0].append(v, mais[i])


n = int(raw_input())

a = map(int, raw_input().split())

mais  = [[] for i in xrange(n+1)]
menos = [[] for i in xrange(n+1)]

for i in xrange(len(a)):
    v = [i, a[i], 0]

    x = i + a[i]
    if x > n:
        mais[0].append(v)
    else:
        mais[x].append(v)   
    
    x = i - a[i]
    if x <= 0:
        menos[0].append(v)
    else: 
        menos[x].append(v)

    soma = bfs(mais, menos)

    for i in len(soma):
        print soma[i]
