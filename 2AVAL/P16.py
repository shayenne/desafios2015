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


n = int(raw_input())
if not n:
    print -1
    exit(0)

graph = {}
for i in xrange(1, n+1):
    graph[i] = set()

for i in xrange(1, n+1):
    x = map(int, raw_input().split())
    for j in xrange(len(x)-1):
        graph[i].add(x[j])
        graph[x[j]].add(i)
        
if GRAPHtwocolor( graph):
    print ''.join(map(str, color[1:len(color)]))
else:
    print -1
