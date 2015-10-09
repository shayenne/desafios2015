#!/usr/bin/env python

vistos = []#[False]*100000

# Existe caminho que liga v a w?
def haCaminho(graph, v, w):
    global vistos
    if v == w:
        return True
    
    vistos[v] = True

    for s in graph[v]:
        if not vistos[s]:
            vistos[s] = True
            return haCaminho(graph, s, w)

    return False

def componentes(graph):
    global vistos
    cnt = 0
    vistos = range(len(graph)+1)
    for v in graph:
        vistos[v] = -1
    for v in graph:
        if vistos[v] == -1:
            cnt += 1
            dfs( graph, v, cnt)
            
    return cnt

def dfs(graph, v, cnt):
    global vistos
    vistos[v] = cnt
    for a in graph[v]:
        if vistos[a] == -1:
            dfs(graph, a, cnt)

def main():
    global vistos
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
        
        if not haCaminho(graph, threads[t][0], threads[t][1]):
            qtdcomp += 1
        
        comp.append(qtdcomp)

    print ' '.join(map(str, comp))




if __name__ == "__main__":
    main()
