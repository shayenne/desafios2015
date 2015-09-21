"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P5 - 1787. Turn for MEGA
"""
#!/usr/bin/env python

k, n = map(int, raw_input().split())

cars = map(int, raw_input().split())

x = 0
for i in xrange(n):
    x += cars[i] - k

    if x < 0:
        x = 0
        
print x
