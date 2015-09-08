# Knuth-Morris-Pratt string matching
# David Eppstein, UC Irvine, 1 Mar 2002

from __future__ import generators

def KMP(text, pattern):

    '''Yields all starting positions of copies of the pattern in the text.
Calling conventions are similar to string.find, but its arguments can be
lists or iterators, not just strings, it returns all matches, not just
the first one, and it does not need the whole text in memory at once.
Whenever it yields, it will have read the text exactly up to and including
the match that caused the yield.'''

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


