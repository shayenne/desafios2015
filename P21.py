#!/usr/bin/env python

import math

W, D = map(int, raw_input().split())

x0, y0 = map(int, raw_input().split())

x1, y1 = map(int, raw_input().split())

seq = list(raw_input())


length = 0
i = 0
j = 0
for k in range(len(seq)):
    if seq[k] == 'F' or seq[k] == 'B':
        j += 1
    else:
        i += 1
        
if i != 0 or j != 0:
    px = math.floor((i + 1)/2)*2*W+math.pow(-1, i)*x0
    py = math.floor((j + 1)/2)*2*D+math.pow(-1, j)*y0

    length = math.sqrt(math.pow(px - x1, 2) + math.pow(py - y1, 2))

print round(length, 4)
