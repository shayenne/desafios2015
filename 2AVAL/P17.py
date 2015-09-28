"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P17 - 1004. Sightseeing Trip
"""
#!/usr/bin/env python

entry = raw_input().split()
while entry[0] != '-1':
    routes = []
    n, m = map(int, entry)

    for i in xrange(m):
        routes.append(map(int, raw_input().split()))

    print n, m
    print routes

    entry = raw_input().split()

