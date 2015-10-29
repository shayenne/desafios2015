"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P1 - 1588. Jamaica
"""

import math

n = int(raw_input())

mapa = []
for i in xrange(n):
    x, y = map(int, raw_input().split())
    mapa.append([x, y])

ang = {}
for i in xrange(n):
    x0, y0 = mapa[i]
    for j in xrange(i+1, n):
        
        x1, y1 = mapa[j]
        co = 1.0*(y1-y0)
        ca = 1.0*(x1-x0)
        
        
        dist = math.sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0))
        #print dist
        if y0 == y1:
            tang = float('inf')
            if x0 < x1:
                proj = 10005+y1
            else:
                proj = 10005+y0
        elif x0 == x1:
            tang = 0
            proj = x0
        else:
            tang = (co/ca)
            proj = (x1*y0 - x0*y1)/(1.0*(y0-y1))
        if (tang, proj) not in ang:
            ang[(tang, proj)] = dist
        elif ang[(tang, proj)] < dist:
            ang[(tang, proj)] = dist

total = 0
for a in ang:
    total += ang[a]

print "{0:.0f}".format(round(total))

    
