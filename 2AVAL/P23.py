"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P16 - 1080. Map Coloring
"""
#!/usr/bin/env python

import sys

color = None

def GRAPHtwocolor( graph):
    global color
    color = [-1]*(len(graph)+1)
    c = 1
    for v in graph:
        if color[v] == -1:
            if not dfsRcolor( graph, v, c):
                return 0
    return 1

def dfsRcolor( graph, v, c):
    color[v] = 1-c
    for w in graph[v]:
        if color[w] == -1:
            if not dfsRcolor( graph, w, 1-c):
                return 0

        elif color[w] == 1-c:
            return 0
    return 1


n, m = map(int, raw_input().split())

graph = {}
for i in xrange(1, 2*n+1):
    graph[i] = []

just = {}
for x in range(2*n):
    just[x] = set()
    
for i in xrange(1, m+1):
    x, y = map(int, raw_input().split())
    graph[x].append(y)
    graph[y].append(x)
    just[x-1].add(y-1)
    just[y-1].add(x-1)

        
if GRAPHtwocolor( graph):
    a = []
    b = []
    for i in xrange(1, len(color)):
        if color[i]:
            a.append(i)
        else:
            b.append(i)
            
    if len(a) < len(b):
        a, b = b, a
    
    while len(a) > len(b):
        
        for x in a:
            for y in b:
                if y-1 not in just[x-1] and len(just[y-1]) + len(b)-1 <= n:
                    b.remove(y)
                    a.append(y)
                    for i in xrange(2*n):
                        if i in just[y-1]:
                            a.remove(i+1)
                            b.append(i+1)
                    break        
            if len(a) == len(b):
                break                           
                
                    
                 
    print ' '.join(map(str, a))
    print ' '.join(map(str, b))
else:
    print "IMPOSSIBLE"
