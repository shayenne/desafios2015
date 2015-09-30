#!/usr/bin/env python

caminho = []

def haNova(rotas, num, encontra, vista, partida):
    i = rotas[num].index(partida)

    while rotas[num][i] != -1:
        x = rotas[num][i]
        #global caminho
        if len(caminho) == 0 or x != caminho[len(caminho)-1]:
            caminho.append(x)
        rotas[num][i] = -1
        #if encontra[x] == set():
        i += 1
        if i == len(rotas[num]):
            i = 2
        #else:
        if encontra[x] != set():
             r = list(encontra[x])[0]
             encontra[x].remove(r)
             if not vista[r]:
                 vista[r] = True
                 haNova(rotas, r, encontra, vista, x)

    return vista


n = int(raw_input())


rotas = []
for i in xrange(n):
    rotas.append(map(int, raw_input().split()))

encontra = {}
for i in xrange(n):
    for ponto in rotas[i]:
        if ponto not in encontra:
            encontra[ponto] = set()
        encontra[ponto].add(i)

vista = [False]*n

vista[0] = True
vista = haNova(rotas, 0, encontra, vista, rotas[0][1])

print caminho
print vista
if False in vista:
    print 0
else:
    print len(caminho), ' '.join(map(str, caminho[0:len(caminho)]))
