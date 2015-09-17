# Shayenne Moura
#!/usr/bin/env python

import sys
# Proximas possiveis:
# pos[i][j]: [i+/-2][j+/-1] e [i+/-1][j+/-2]
def ContaPossiveis(i, j, tab):
    ki = [2, -2,  2, -2, 1, -1,  1, -1]
    kj = [1,  1, -1, -1, 2,  2, -2, -2]
    cnt = 0

    for l in xrange(8):
        if i+ki[l] >= 0 and i+ki[l] < len(tab) and j+kj[l] >= 0 and j+kj[l] < len(tab) and not tab[i+ki[l]][j+kj[l]]:
            cnt += 1

    return cnt

def ResolvePara(i, j, tab, qtd):
    ki = [2, -2,  2, -2, 1, -1,  1, -1]
    kj = [1,  1, -1, -1, 2,  2, -2, -2]
    letra = ["a", "b", "c", "d", "e", "f", "g", "h"]
    way = []
    for k in xrange(8):
        if i+ki[k] >= 0 and i+ki[k] < len(tab) and j+kj[k] >= 0 and j+kj[k] < len(tab) and not tab[i+ki[k]][j+kj[k]]:
            way.append([i+ki[k], j+kj[k], ContaPossiveis(i+ki[k], j+kj[k], tab)])    
    
    way.sort(key=lambda tup: tup[2])
    if len(way) == 0:
        if qtd == n*n:
            return True
        else:
            return False
        
    k = 0
    while k < len(way):
        tab[way[k][0]][way[k][1]] = 1
        if ResolvePara(way[k][0], way[k][1], tab, qtd+1):
            print "{}{}".format(letra[way[k][0]], way[k][1]+1)
            return True
        else:
            tab[way[k][0]][way[k][1]] = 0
            k += 1


    return False

n = int(raw_input())

tab = []
for i in xrange(n):
    tab.append([])
    for j in xrange(n):
        tab[i].append(0)


tab[0][0] = 1

if ResolvePara(0, 0, tab, 1):
    print "a{}".format(tab[0][0])
else:
    print "IMPOSSIBLE"
