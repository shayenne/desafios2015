
"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
2a aval
Problema P21 - 1213. Cockroaches!
"""

def percorreGrafo(graph, ini):
	vistos = [ini]
	ver = [ini]
	count = 0
	while ver != []:
		new = []
		for x in ver:	
			for v in graph[x]:	
				if v not in vistos:
					vistos.append(v)	
					new.append(v)
					count += 1
		ver = new
	return count

graph = {}

floodgate = raw_input()

line = raw_input()
nGraph = False
n = 0
while line != "#":
	nGraph = True
	line = line.split("-")
	if line[0] not in graph:
		graph[line[0]] = []
		n+= 1
	if line[1] not in graph:
		graph[line[1]] = []
		n+=1
	graph[line[0]].append(line[1])
	graph[line[1]].append(line[0])
	
	line = raw_input()
	
if nGraph:	
	#if percorreGrafo(graph, floodgate) != n-1:
	#	print n-1
	#else:
	print percorreGrafo(graph, floodgate)	
else:
	print 0
