#!/usr/bin/env python

g = []

t = []

r = []

n, m = map(int, raw_input().split())

for i in xrange(n):
    g.append(i)

for i in xrange(m):
    t.append(map(int, raw_input().split()))

s = int(raw_input())

r = map(int, raw_input().split())

for i in xrange(1, m+1):
    if i not in r:
        x = t[i-1][0]
        y = t[i-1][1]
        if x > y:
           for j in xrange(n):
               if g[j] == y:
                   g[j] = x
        else:
           for j in xrange(n):
               if g[j] == x:
                   g[j] = y


ord = []
for i in xrange(len(r)-1, -1, -1):
    x = t[r[i]-1][0]
    y = t[r[i]-1][1]
    if x > y:
        for j in xrange(n):
            if g[j] == y:
                g[j] = x
    else:
        for j in xrange(n):
            if g[j] == x:
                g[j] = y
  
    ord.append(len(set(g)))

ord.reverse()
print ' '.join(map(str, ord))
