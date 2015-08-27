#!/usr/bin/env/ python

_end = '_end_'

def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

def in_trie(trie, word):
     current_dict = trie
     for letter in word:
         if letter in current_dict:
             current_dict = current_dict[letter]
         else:
             return False
     else:
         if _end in current_dict:
             return True
         else:
             return False

lista = []

word = str(raw_input())
for i in range(len(word)+1):
    for j in range(len(word)+1):
        if len(word[i:j]) > 0:
            lista.append(str(word[i:j]))


        
trie = make_trie(lista)
print make_trie(lista)
print lista
print make_trie('foo', 'bar', 'bara', 'barz')

count = 0
for i in range(len(lista)):
    if in_trie(trie, lista[i]) == True:
        count += 1

print count
