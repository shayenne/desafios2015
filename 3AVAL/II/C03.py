9-

n, m, k = map(int, raw_input().split())

a = map(int, raw_input().split())

for i in xrange(m):
    dic[i] = map(int, raw_input().split())

for i in range(n):
	x, y = map(int, raw_input().split())
	x += 1
	nivel[get(x)] += 1
	set(x, 1)

for i in range(n):
	print nivel[i]
