#!/usr/bin/env python

import sys
# Proximas possiveis:
# pos[i][j]: [i+/-2][j+/-1] e [i+/-1][j+/-2]
def ContaPossiveis(i, j, tab):
    ki = [2, -2,  2, -2, 1, -1,  1, -1]
    kj = [1,  1, -1, -1, 2,  2, -2, -2]
    cnt = 0
    print i, j
    for l in xrange(8):
        if i+ki[l] >= 0 and i+ki[l] < len(tab) and j+kj[l] >= 0 and j+kj[l] < len(tab) and not tab[i+ki[l]][j+kj[l]]:
            cnt += 1

    return cnt

def ResolvePara(i, j, tab):
    ki = [2, -2,  2, -2, 1, -1,  1, -1]
    kj = [1,  1, -1, -1, 2,  2, -2, -2]
    way = []
    for k in xrange(8):
        if i+ki[k] >= 0 and i+ki[k] < len(tab) and j+kj[k] >= 0 and j+kj[k] < len(tab) and not tab[i+ki[k]][j+kj[k]]:
            way.append([i+ki[k], j+kj[k], ContaPossiveis(i+ki[k], j+kj[k], tab)])
    print way
    
    
    way.sort(key=lambda tup: tup[2])
    if len(way) == 0:
        return False
    k = 0
    while k < len(way):
        tab[way[k][0]][way[k][1]] = 1
        ResolvePara(way[k][0], way[k][1], tab)
        return 

    return False

n = int(raw_input())

tab = []
for i in xrange(n):
    tab.append([])
    for j in xrange(n):
        tab[i].append(0)


tab[0][0] = 1
print tab

if ResolvePara(0, 0, tab):
    print "SIM"
else:
    print "NAO"
