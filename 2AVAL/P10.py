#!/usr/bin/env python

def removeParents(v, p, s):
    if v not in p:
        s.remove(v)
        return

    for x in p[v]:
        removeParents(x, p, s)
    
    del p[x]

def removeChildren(v, c, s):
    if v not in c:
        s.remove(v)
        return

    if x in c[v]:
        removeChildren(x, c, s)
    del c[x]


            
n = int(raw_input())

parents = {}
children = {}

entr = raw_input()
while entr != 'BLOOD':
    x, y = map(int, entr.split())
    if y not in parents:
        parents[y] = set()
    if x not in children:
        children[x] = set() 
    parents[y].add(x)
    children[x].add(y)
    entr = raw_input()

print parents, children

suspect = set()

for i in xrange(n):
    suspect.add(i)

victim = int(raw_input())
while (victim != ""):
    removeParents(victim, parents, suspect)
    removeChildren(victim, children, suspect)
    suspect.remove(victim)
    victim = raw_input()

print parents, children
print suspect
