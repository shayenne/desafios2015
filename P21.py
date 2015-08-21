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

if i % 2 == 0:
    px = i*W+x0
else:
    px = (i+1)*W-x0

if j % 2 == 0:
    py = j*D+y0
else:
    py = (j+1)*D-y0

length = math.sqrt((px - x1)*(px - x1) + (py - y1)*(py - y1))

print round(length, 4)
