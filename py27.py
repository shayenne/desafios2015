# Shayenne Moura
#!/usr/bin/env python

MAX = 32005

n = int(raw_input())

nivel = [0]*MAX
T = [0]*MAX

def get(i):
	s = 0
	while i > 0:
		s += T[i]
		i -= i&(-i)
	return s

def set(pos, val):
	while pos <= MAX:
		T[pos] += val
		pos += pos&(-pos)



for i in range(n):
	x, y = map(int, raw_input().split())
	x += 1
	nivel[get(x)] += 1
	set(x, 1)

for i in range(n):
	print nivel[i]

