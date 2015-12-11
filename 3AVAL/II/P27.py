grafo = []
qtd = []

lvr = [0 for i in xrange(201)]

def dfsBigPath(g, v, ini):
    global lvr, grafo, qtd
    maxv = -1
    
    if v != ini and qtd[v] <= 1:
        return 0

    lvr[v] = 1

    for w in g[v]:
        if lvr[w] == 0 and grafo[v][w] == 1:
            maxw = dfsBigPath(g, w, ini)
            if maxw != -1 and maxv < 1 + maxw:
                maxv = 1 + maxw

    lvr[v] = 0
    return maxv


livres = []

def verticesLivres(g, v, ini):
    global livres, grafo, qtd
    if v != ini and qtd[v] <= 1:
        livres.append(v)
        return

    lvr[v] = 1
    for w in g[v]:
        if lvr[w] == 0 and grafo[v][w] == 1:
            verticesLivres(g, w, ini)

    lvr[v] = 0




def bigPath(g, v):
    global view, lvr, livres, grafo
    for x in g:
        lvr[x] = 0

    big = 0
    livres = []
    verticesLivres(g, v, v)

    for l in livres:
        
        for x in g:
            lvr[x] = 0
        path = dfsBigPath(g, l, l)
        if path > big:
            big = path

    return big



n = int(raw_input())

graph = {}
grafo = [[0 for i in xrange(n+1)] for i in xrange(n+1)]
qtd = [0 for i in xrange(n+1)]
arestas = [[0 for i in xrange(n+1)] for i in xrange(n+1)]
for i in xrange(n-1):
    a, b = map(int, raw_input().split())

    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()

    graph[a].add(b)
    graph[b].add(a)
    grafo[a][b] = 1
    grafo[b][a] = 1
    qtd[a] += 1
    qtd[b] += 1


maior = 0
#print arestas
for v in graph:
    for w in graph[v]:
        if arestas[v][w] != 1:
            arestas[v][w] = 1
            arestas[w][v] = 1
            qtd[v] -= 1
            qtd[w] -= 1
            grafo[v][w] = 0
            grafo[w][v] = 0

            #graph[v].remove(w)
            #graph[w].remove(v)
            
            v1 = bigPath(graph, v)
            v2 = bigPath(graph, w)
            v1 *= v2
            if v1 > maior:
                maior = v1
                
            #graph[v].add(w)
            #graph[w].add(v)
            qtd[v] += 1
            qtd[w] += 1
            grafo[v][w] = 1
            grafo[w][v] = 1
        
print maior
