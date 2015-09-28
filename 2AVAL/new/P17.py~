"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P8 - 1837. Isenbaev's Number
"""
#!/usr/bin/env python

def caminha(lst, graph, index, dist):
    busca = []
    for people in lst:
        if dist[people] == 'undefined' or dist[people] > index:
            busca.append(people)
            dist[people] = index
                
    for people in busca:
            caminha(graph[people], graph, index+1, dist)
            

n = int(raw_input())

graph = {}
index = {}
visited = []

for i in xrange(n):
    x, y, z  = raw_input().split()
    if x not in graph:
        graph[x] = set()
    if y not in graph:
        graph[y] = set()
    if z not in graph:
        graph[z] = set()
    graph[x].add(y)
    graph[x].add(z)
    graph[y].add(x)
    graph[y].add(z)
    graph[z].add(x)
    graph[z].add(y)
    

ordem = []
nomes = {}
for people in graph:
    nomes[people] = 'undefined'

if 'Isenbaev' in graph:
    nomes['Isenbaev'] = 0
    for people in graph:
        caminha(graph['Isenbaev'], graph, 1, nomes)

for people in graph:
    ordem.append([people, nomes[people]])

ordem.sort(key = lambda tup: tup[0])
    
for x in ordem:
    print x[0], x[1]
