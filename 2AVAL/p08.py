#!/usr/bin/env python

#from sets import Set as set

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return []

def caminha(lst, graph, index, dist):
    for people in lst:
        if dist[people] != 'undefined':
            if dist[people] > index:
                dist[people] = index
            return
        else:
            dist[people] = index
            caminha(graph[people], graph, index+1, dist)
        

n = int(raw_input())

graph = {}
index = {}
names = []

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
    


for people in graph:
            
    if people == 'Isenbaev':
        names.append([people, 0])
    else:
        if 'Isenbaev' in graph:
            num = len(shortest_path(graph, 'Isenbaev', people))
            if num > 0:
                names.append([people, num-1])
            else:
                names.append([people, 'undefined'])
        else:
            names.append([people, 'undefined'])

names.sort(key = lambda tup:tup[0])

for name in names:
    print name[0], name[1]
    
nomes = {}
for people in graph:
    nomes[people] = 'undefined'

for people in graph:
    if 'Isenbaev' in graph:
        caminha(graph['Isenbaev'], graph, 0, nomes)

for nome in nomes:
    print nome, nomes[nome]
