"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P9 - 1020. Rope 
"""

import math

x = raw_input().split()

n, r = int(x[0]), float(x[1])


dist = 0
if n > 0:
    x, y = map(float, raw_input().split())

fx, fy = x, y
    
for i in xrange(n-1):
    k, l = x, y
    x, y = map(float, raw_input().split())

    dist += math.sqrt((x-k)*(x-k) + (y-l)*(y-l))

dist += math.sqrt((x-fx)*(x-fx) + (y-fy)*(y-fy))

dist += 2 * r * math.pi


print "{0:.2f}".format(dist)
