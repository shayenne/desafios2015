#!/usr/bin/env python

import sys

n, m = map(int, raw_input().split())
while n != 0:
	next = False
# Inicializa o vetor com as posicoes de 1 a n
	lista = [[0, [], x] for x in range(n)]

	for i in range(m):
		a, b = map(int, raw_input().split())
		lista[a-1][0] += 1
		lista[a-1][1].append(b-1)

		if lista[b-1][1].count(a-1) > 0:
			print "IMPOSSIBLE"
			next = True


	if not next:
		lista.sort(key=lambda tup: tup[2])
		for i in range(n):
			print lista[i][2]+1
	
		
	
	n, m = map(int, raw_input().split())


