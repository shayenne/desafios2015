# Shayenne Moura
#!/usr/bin/env python

n = int(raw_input())

if n < 4:
	print "NO"
	
else:
	print "YES"
	if (n % 2) == 0:
		print "2 * 3 = 6"
		print "6 * 4 = 24"
		print "1 * 24 = 24"
		for i in range(5, n, 2):
			print i+1, "-", i, "=", 1
			print "1 * 24 = 24"
	else:
		print "5 * 4 = 20"
		print "20 + 3 = 23"
		print "2 - 1 = 1"
		print "23 + 1 = 24"
		for i in range(6, n, 2):
			print i+1, "-", i, "=", 1
			print "1 * 24 = 24"
