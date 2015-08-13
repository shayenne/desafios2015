#!/usr/bin/env python

from sys import exit

order = []

n = int(raw_input())
parts = []

for i in range(n):
    tmp = raw_input()
    parts.append(tmp.split() + [i+1])

m = int(raw_input())
actors = []

for i in range(m):
    tmp = raw_input()
    actors.append(tmp.split() + [i+1])


for part in parts:
    part.append(0)
    for actor in actors:
        if part[0] >= actor[0] and part[1] <= actor[1]:
            part[3] += 1


parts.sort(key=lambda tup: tup[3])
actors.sort(key=lambda tup: tup[2])
            
print parts
print actors

i = 0
j = 0
cont = 0

for i in range(n):
    for j in range(m):
        if actors[j][2] > 0 and parts[i][0] >= actors[j][0] and parts[i][1] <= actors[j][1]:
            order.append([parts[i][2],actors[j][3]])
            actors[j][2] = int(actors[j][2]) - 1
            break
    try:
        order[i]
    except IndexError:
        print order
        print "NO"
        exit(0)
    

"""

i = 0
cnt = -1
while i < range(len(parts)) and len(parts) > 0:
    cnt += 1
    j = 0
    print i, len(parts)
    while j < range(len(actors)) and len(actors) > 0:
        print i, j, len(parts)
        print parts
        print actors
        if parts[i][0] >= actors[j][0] and parts[i][1] <= actors[j][1]:
            order.append([parts[i][2],actors[j][3]])
            del parts[i]
            actors[j][2] = int(actors[j][2]) - 1
            if actors[j][2] == 0:
                del actors[j]
                break
            else:
                break
        else:
            j += 1

    i+=1


    try:
        order[cnt]
    except IndexError:
        print "NO"
        exit(0)




    
"""

"""
    try:
        order[i]
    except IndexError:
        print "NO"
        exit(0)
"""


order.sort(key=lambda tup: tup[0])       
        
            
print "YES"
print " ".join(str(order[x][1]) for x in range(n))



"""      
for i in range(n):
    for j in range(m):
        if parts[i][0] >= actors[j][0] and parts[i][1] <= actors[j][1]:
            order.append([actors[j][3], parts[i][2]])
            actors[j][2] = int(actors[j][2]) - 1
            if actors[j][2] == 0:
                del actors[j]
                m -= 1
            break
    try:
        order[i]
    except IndexError:
        print "NO"
        exit(0)

order.sort(key=lambda tup: tup[1])       
        
            
print "YES"
print " ".join(str(order[x][0]) for x in range(n))
"""
