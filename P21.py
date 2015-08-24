#!/usr/bin/env python

import math

W, D = map(int, raw_input().split())

x0, y0 = map(int, raw_input().split())

x1, y1 = map(int, raw_input().split())

seq = list(raw_input())


length = 0
idi = 0
idj = 0
i = 0
j = 0
for k in range(len(seq)):
    if seq[k] == 'F' or seq[k] == 'B':
        if seq[k] == 'B' and idj == 0 and j == 0:
            idj = -1
        j += 1
    else:
        if seq[k] == 'R' and idi == 0 and i == 0:
            idi = -1
        i += 1

if idi != 0:
    i *= idi
    
if idj != 0:
    j *= idj
        
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
