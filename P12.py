# Shayenne Moura
#!/usr/bin/env python

def conta_paredes(m, i, j):
	if (m[i][j] == 1):
		return 0;
	cnt = 0
	m[i][j] = 1
	if (j + 1 < len(m) and m[i][j+1] == "#") or j+1 == len(m):
		cnt += 1
	else:
		cnt += conta_paredes(m, i, j+1)
	if (i + 1 < len(m) and m[i+1][j] == "#") or i+1 == len(m):
		cnt += 1
	else:
		cnt += conta_paredes(m, i+1, j)
	if (j - 1 >= 0 and m[i][j-1] == "#") or j - 1 < 0:
		cnt += 1
	else:
		cnt += conta_paredes(m, i, j-1)
	if (i - 1 >= 0 and m[i-1][j] == "#") or i - 1 < 0:
		cnt += 1
	else:
		cnt += conta_paredes(m, i-1, j)
	
	return cnt;


n = int(raw_input())
matrix = []

area = 0

for i in range(n):
	matrix.append(list(raw_input()));


area = conta_paredes(matrix, 0, 0)


if matrix[n-1][n-1] != 1:
	area += conta_paredes(matrix, n-1, n-1)

area -= 4
print area * 9

