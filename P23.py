# Shayenne Moura
# Baseado em Knuth-Morris-Pratt string matching
# David Eppstein, UC Irvine, 1 Mar 2002

from __future__ import generators

def KMP(text, pattern):

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen > 0:
            yield startPos
            

pat = raw_input()
text = raw_input()
lista = []
for i in KMP(text, pat):
	lista.append(i)

word = []

if len(lista) < len(text):
	print "Yes"
else:
	print "No"
	first = lista[0];
	for i in range(len(lista)):
		if(lista[i] != first):
			word.append(text[first:lista[i]])
			first = lista[i]
	word.append(text[first:len(lista)])
	print ' '.join(word)


