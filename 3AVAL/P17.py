"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P17 - 1207. Median on the Plane
"""

global ymenor 

def compare(p, q):
    global ymenor
    if p == ymenor:
        return 1
    elif q == ymenor:
        return -1
    
    x1, y1 = ymenor[0:2]
    x2, y2 = p[0:2]
    x3, y3 = q[0:2]
    res = (x2-x1) * (y3-y1) - (x3-x1) * (y2-y1)
    if res < 0:
        return -1
    elif res > 0:
        return 1
    else:
        return 0
    
n = int(raw_input())

ymenor = []

points = []

for i in xrange(n):
    x, y = map(int, raw_input().split())
    points.append([x, y, i+1])
    if ymenor == [] or y < ymenor[1]:
        ymenor = [x, y, i+1]
    #elif y == ymenor[1] and x < ymenor[0]:
    #    ymenor = [x, y, i+1]

#print ymenor
points.sort(compare)

#print points
print points[n-1][2], points[((n-2)/2)][2]

            
