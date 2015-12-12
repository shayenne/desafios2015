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
    for i in xrange(len(menos[v])):
        print menos, v, i, menos[v]
        if menos[v] is not [] and menos[v][i][2] == 0:
            fila[0].append([v, menos[i]])

    for i in xrange(len(mais[v])):
        print mais
        if mais[v][i][2] == 0:
            fila[0].append(v, mais[i])

    ind = 0
    while fila[0] is not [] or fila[1] is not []:
        if fila[ind] is []:
            if ind == 0:
                ind = 1
            else:
                ind = 0

        v = fila[ind].pop()
        print v
        v[2] = 1
        
        if ind == 0:
            adj = mais
            dc = 1
        else:
            adj = menos
            dc = 0

        for it in adj[v[1]]:
            if not it[2]:
                it[1] += it[1]
                if it[2] == 1:
                    soma[it[0]] = it[1]

                else:
                    fila[dc].append(it[0], it)

        ind = dc

    return soma

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

    for i in xrange(len(soma)):
        print soma[i]
