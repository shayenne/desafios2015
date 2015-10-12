"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P27
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

if not n:
    print -1
    exit(0)

graph = {}
for i in xrange(0, n*m + 1):
    graph[i] = []

ant = map(int, raw_input().split())
for j in xrange(1, len(ant)):
    graph[j-1].append(j)
    graph[j].append(j-1)

i = m
for i in xrange(1, n):
    x = map(int, raw_input().split())
    for j in xrange(1, len(x)):
        graph[i+j-1].append(i+j)
        graph[i+j].append(i+j-1)
    for j in xrange(len(x)):
        graph[(i-m)+j].append(i+j)
        graph[i+j].append((i-m)+j)
    i += m

print graph
if GRAPHtwocolor( graph):
    print ''.join(map(str, color[1:len(color)]))
else:
    print -1
