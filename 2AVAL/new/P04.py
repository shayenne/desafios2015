"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P4 - 1607. Taxi
"""
#!/usr/bin/env python

import math as m
import sys

a, ra, b, rb = map(int, raw_input().split())

n = (b - a) / (ra + rb) + 1 

if a > b:
    print a
    exit(0)
    
an = a + n * ra
bn = b - (n - 1) * rb

if an > bn:
    print bn  
else:
    print an
