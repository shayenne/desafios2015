#!/usr/bin/env python

import sys

caminho = []

def haNova(rotas, num, encontra, vista, partida):
    i = rotas[num].index(partida)

    while rotas[num][i] != -1:
        x = rotas[num][i]
        #global caminho
        if len(caminho) == 0 or x != caminho[len(caminho)-1]:
            caminho.append(x)
	if i == 1:
            rotas[num][len(rotas[num])-1] = -1
        rotas[num][i] = -1
        #if encontra[x] == set():
        i += 1
        if i == len(rotas[num]):
            rotas[num][1] = -1
            i = 2
        #else:
	
        if len(encontra[x]) > 1:
             r = list(encontra[x])[0]
             if r == num:
                 r = list(encontra[x])[1]
             encontra[x].remove(r)
             if not vista[r]:
                 vista[r] = True
                 haNova(rotas, r, encontra, vista, x)
                 caminho.append(x)

    return vista



all_input = iter(sys.stdin.read().strip().replace('\n', ' ').split(' '))


n = int(all_input.next())
rotas = []
for i in xrange(n):
    m = int(all_input.next())
    rotas.append([m])
    u = all_input.next()
    rotas[i].append(u)
    for j in xrange(m):
        v = all_input.next()
        rotas[i].append(v)





#n = int(raw_input())


#rotas = []
#for i in xrange(n):
#    rotas.append(map(int, raw_input().split()))

encontra = {}
for i in xrange(n):
    for ponto in rotas[i][1:len(rotas[i])]:
        if ponto not in encontra:
            encontra[ponto] = set()
        encontra[ponto].add(i)

#print rotas, encontra

vista = [False]*n

vista[0] = True
vista = haNova(rotas, 0, encontra, vista, rotas[0][1])

#print caminho
#print vista
if False in vista:
    print 0
else:
    print len(caminho), ' '.join(map(str, caminho)), caminho[0]
