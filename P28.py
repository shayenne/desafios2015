#!/usr/bin/env/ python
"""
_end = '_end_'

def make_trie():
    root = dict()
    return root

def insert_trie(trie, word, count):
    root = trie
    current_dict = root
    for letter in word:
        if current_dict.setdefault(letter, {}) == {}:
            count += 1
        current_dict = current_dict.setdefault(letter, 0)
    current_dict[_end] = _end
    return count


trie = make_trie()
x = 0
word = str(raw_input())

for i in range(len(word)+1):
    for j in range(len(word)+1):
        if len(word[i:j]) > 0:
            x = insert_trie(trie, str(word[i:j]), x)

print x

"""

def insere(word, v):
    e = 0
    d = len(v)-1
    while e <= d:
        m = int((e+d)/2)
        if word == v[m]:
            return 0
           
        if word > v[m]:
            if m+1 < len(v) and word < v[m+1]:
                v.insert(m+1, word)
                return 1
            e = m + 1
        else:
            if m-1 >= 0 and word > v[m-1]:
                v.insert(m, word)
                return 1
            d = m - 1
    v.append(word)
    return 1
    

word = raw_input()

x = 0
lista = []
for i in range(len(word)+1):
    for j in range(len(word)+1):
        if len(word[i:j]) > 0:
            x += insere(word[i:j], lista)


print x
