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
