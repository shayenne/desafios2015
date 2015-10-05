

def sign(a):
	s = False
	i = 0
	while i < 15:
		if i != a[i]:
			i, a[i] = a[i], i
			s = not s
		#else: 
		i += 1
			
	return s
	
	
	
n = int(raw_input())

ini = []
for i in xrange(4):
	ini += map(int, raw_input().split())	
	
	
	
a = range(15)+[0]

print a, ini

print sign(a), sign(ini)
