#!/usr/bin/env python

n = int(raw_input())

paint = []
for i in range(n):
    x = raw_input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    paint.append(x)

def busca_binaria_ini(x, v):
    e = 0
    d = len(v)-1
    while e <= d:
        m = (e+d)/2
        if v[m][0] <= x and v[m][1] > x:
            return m
        if v[m][1] < x:
            e = m + 1
        else:
            d = m - 1
    return 0

def busca_binaria_fim(x, v):
    e = 0
    d = len(v)-1
    while e <= d:
        m = (e+d)/2
        if v[m][1] >= x and v[m][0] < x:
            return m
        if v[m][0] < x:
            e = m + 1
        else:
            d = m - 1
    return 0

faixas = [[0, 1000000000, 'w']]

numfaixas = 1

for i in range(n):
    
    ant = busca_binaria_ini(paint[i][0], faixas)
    pos = busca_binaria_fim(paint[i][1], faixas)
    """
    ant = 0
    while faixas[ant][1] < paint[i][0]:
        ant += 1
    
    pos = ant
    while faixas[pos][1] < paint[i][1]:
        pos += 1
    """

    # Olha para a nova pintura e para onde ficam o inicio e o fim
    # Ambos os extremos estao em uma unica faixa
    if ant == pos:
        # A pintura e de cor diferente da faixa em questao
        if paint[i][2] != faixas[ant][2]:
            faixas.insert(ant+1, [paint[i][1], faixas[ant][1], faixas[ant][2]])
            faixas.insert(ant+1, paint[i])
            faixas[ant][1] = paint[i][0]
    # Os extremos estao em faixas diferentes
    else:
        # As faixas possuem cores iguais
        if faixas[ant][2] == faixas[pos][2]:
            # A pintura e da mesma cor das faixas
            if faixas[ant][2] == paint[i][2]:
                faixas[pos][0] = faixas[ant][0]
                del faixas[ant:pos]
            # A pintura e de cor diferente
            else:
                faixas[ant][1] = paint[i][0]
                faixas[pos][0] = paint[i][1]
                del faixas[ant+1:pos]
                faixas.insert(ant+1, paint[i])
            
        # As faixas possuem cores diferentes
        else:
            # A nova e da cor da primeira
            if paint[i][2] == faixas[ant][2]:
                faixas[pos][0] = paint[i][1]
                faixas[ant][1] = paint[i][1]
                del faixas[ant+1:pos]
            # A nova e da cor da segunda
            else:
                faixas[ant][1] = paint[i][0]
                faixas[pos][0] = paint[i][0]
                del faixas[ant+1:pos]


fmax = [0, 0, 0]
for faixa in faixas:
    if faixa[2] == 'w':
        val = faixa[1] - faixa[0]
        if val > fmax[2]:
            fmax = faixa
            fmax[2] = val


print fmax[0], fmax[1] 

