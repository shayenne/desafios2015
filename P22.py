#!/usr/bin/env python

import heapq

class MyPriQueue(object):
    def __init__(self):
        self.heap = []

    def add(self, d):
        heapq.heappush(self.heap, d)

    def get(self):
        d = heapq.heappop(self.heap)
        return d
        
    def pushpop(self, d):
        heapq.heappushpop(self.heap, d)

    def empty(self):
        return self.heap == []

    def largest(self):
        return heapq.nlargest(1, self.heap);

    def smallest(self, n):
        return heapq.nsmallest(n, self.heap);


n = int(raw_input())

q = MyPriQueue()
for i in range(n):
	x = int(raw_input())
	if i >= (n/2)+1:
		q.pushpop(x)
	else:
		q.add(x)

if n % 2:
	[x] = q.smallest(1)
	print x
else:
	x, y = q.smallest(2)
	
	print '{0:.1f}'.format((float)(x+y)/2)
