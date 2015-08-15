#!/usr/bin/env python

from sys import exit

order = []

n = int(raw_input())
parts = []

for i in range(n):
    tmp = map(int, raw_input().split())
    parts.append(tmp + [i+1])

m = int(raw_input())
actors = []

for i in range(m):
    tmp = map(int, raw_input().split())
    actors.append(tmp + [i+1])


parts.sort(key=lambda tup: tup[0])
actors.sort(key=lambda tup: tup[1])


for i in range(n):
    j = 0
    while j < len(actors):
        if parts[i][0] >= actors[j][0] and parts[i][1] <= actors[j][1]:
            order.append([parts[i][2],actors[j][3]])
            actors[j][2] = int(actors[j][2]) - 1
            if actors[j][2] == 0:
                del actors[j]
                j -= 1
            break
        j += 1
    try:
        order[i]
    except IndexError:
        print "NO"
        exit(0)
    

order.sort(key=lambda tup: tup[0])       
        
            
print "YES"
print " ".join(str(order[x][1]) for x in range(n))



