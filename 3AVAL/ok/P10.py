"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P10- 1084. Goat in the Garden
"""
import math


l, r = map(float, raw_input().split())

area = 0

if r <= l/2:
    area = math.pi*r*r

elif r >= (l*math.sqrt(2))/2.0:
    area = l*l
    
else:
    theta = math.acos(l/r/2)

    circ = math.pi*r*r

    borda = r*r/2.0*(2*theta - math.sin(2*theta))

    area = circ - 4*borda

print "{0:.3f}".format(area)
