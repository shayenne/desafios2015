#!/usr/bin/env python

palindrome = raw_input()

n = len(palindrome)

cnt = 1
aux = 0

i = n-1
j = 0

while i < n and j < n and palindrome[i] == palindrome[j]:
	aux += 1
	i -= 1
	j += 1

if aux == n:
	print "1"
	print palindrome 

lista = []

i = n-1
j = 1

while j < n:

	while i < n and j < n and palindrome[i] == palindrome[j]:
		aux += 1
		i -= 1
		j += 1

	if aux > cnt and i+1 <= lista[len(lista)-1][0]+lista[len(lista)-1][1]:
		lista.append([aux, i+1])
		cnt = aux

	i = 0
	j += 1
