#!/usr/bin/env/ python

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

