t = int(raw_input())

A = B = []

graph = {}
for i in xrange(t):
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())

    n = A[0]
    m = B[0]
    A = A[1:]
    B = B[1:]
    for j in xrange(n):
        for k in xrange(m):
            if B[k] % A[j] == 0:
                if A[j] not in graph:
                    graph[A[j]] = []
                graph[A[j]].append(B[k])
                if B[k] not in graph:
                    graph[B[k]] = []
                graph[B[k]].append(A[j])


    print graph
