"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P10 - 1126. Magnetic Storm
"""

import heapq as q

m = int(raw_input())

pq = []

tam = 1
x = raw_input()

while x != "-1":
    x = int(x)
    q.heappush(pq, [(-1)*x, tam])

    if tam >= m:
        l = q.heappop(pq)
        q.heappush(pq, l)
        while pq != [] and tam - l[1] >=  m:
            l = q.heappop(pq)
        q.heappush(pq, l)
        print (-1)*l[0]
            
    
    tam += 1
    
    x  = raw_input()
