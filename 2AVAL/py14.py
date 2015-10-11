#!/usr/bin/env python

count = 0

def find(g, x):
    while x != g[x]:
        x = g[x]
    return x

def Union(g, size, x, y):
    global count
    rootx = find(g, x)
    rooty = find(g, y)

    if rootx == rooty:
        return
    if size[rootx] < size[rooty]:
        g[rootx] = rooty
        size[rooty] += size[rootx]
    else:
        g[rooty] = rootx
        size[rootx] += size[rooty]

    count -= 1

def defineRepresentantes(graph, g, size):
    num = 0
    visto = []

    for i in xrange(len(graph)):
        tam = 0
        if len(visto) == len(graph):
            break
        if i not in visto:
            ver = graph[i]
            visto.append(i)
            tam += 1
            #g[i] = i
            
            num += 1
            while ver != []:
                x = ver.pop()
                if x not in visto:
                    visto.append(x)
                    ver += graph[x]
                    g[x] = i
                    tam += 1
            size[i] = tam

    return num
g = []

size = []

t = []

r = []

n, m = map(int, raw_input().split())
count = n


graph = {}
for i in xrange(n):
    g.append(i)
    size.append(1)
    graph[i] = []



for i in xrange(m):
    x, y = map(int, raw_input().split())
    t.append([x-1, y-1])

s = int(raw_input())

r = map(int, raw_input().split())

for i in xrange(s):
    r[i] -= 1

for i in xrange(m):
    if i not in r:
        Union(g, size, t[i][0], t[i][1])
        #graph[t[i][0]].append(t[i][1])
        #graph[t[i][1]].append(t[i][0])

#count = defineRepresentantes(graph, g, size)
#print num, count

ord = []

ord.append(count)

for i in xrange(len(r)-1, 0, -1):
    if g[t[r[i]][0]] != g[t[r[i]][1]]:
        Union(g, size, t[r[i]][0], t[r[i]][1])
    
    ord.append(count)



ord.reverse()
print ' '.join(map(str, ord))
