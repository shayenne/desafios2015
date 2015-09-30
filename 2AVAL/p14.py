#!/usr/bin/env python

# Existe caminho que liga v a w?
def haCaminho(graph, v, w, vistos):

    if v == w:
        return True
    
    vistos[v] = True

    for s in graph[v]:
        if not vistos[s]:
            vistos[s] = True
            return haCaminho(graph, s, w, vistos)

    return False

def componentes(graph):
    cnt = 0
    visto = range(len(graph)+1)
    for v in graph:
        visto[v] = -1
    for v in graph:
        if visto[v] == -1:
            cnt += 1
            dfs( graph, v, cnt, visto)
            
    return cnt

def dfs(graph, v, cnt, visto):
    visto[v] = cnt
    for a in graph[v]:
        if visto[a] == -1:
            dfs(graph, a, cnt, visto)
        

n, m = map(int, raw_input().split())

graph = {}
threads = [[0, 0]]

for i in range(1, n+1):
    graph[i] = [] 

for i in range(m):
    v, w = map(int, raw_input().split())
    graph[v].append(w)
    graph[w].append(v)
    threads.append([v, w])

t = int(raw_input())

remove = map(int, raw_input().split())

qtdcomp = componentes(graph)

comp = []

for t in remove:
    vistos = [False]*(len(graph)+1)
    if threads[t][0] in graph and threads[t][1] in graph[threads[t][0]]:
        graph[threads[t][0]].remove(threads[t][1])
        graph[threads[t][1]].remove(threads[t][0])
        
    if not haCaminho(graph, threads[t][0], threads[t][1], vistos):
        qtdcomp += 1
        
    comp.append(qtdcomp)

print ' '.join(map(str, comp))
