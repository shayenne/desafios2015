


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
		graph[line[0]] = set()
		n+= 1
	if line[1] not in graph:
		graph[line[1]] = set()
		n+=1
	graph[line[0]].add(line[1])
	graph[line[1]].add(line[0])
	
	line = raw_input()
	
if nGraph:	
	if percorreGrafo(graph, floodgate) != n-1:
		print n-1
	else:
		print percorreGrafo(graph, floodgate)	
else:
	print 0
