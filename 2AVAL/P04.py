#!/usr/bin/env python

n = int(raw_input())

sudoku = []
for i in xrange(n):
    x = map(int, raw_input().split())
    sudoku.append(x)

print sudoku
