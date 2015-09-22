#!/usr/bin/env python

def removeParents(v, p, s):
    if v not in p:
        if v in s:
            s.remove(v)
        return

    for x in p[v]:
        if x in s: 
            s.remove(x)
        removeParents(x, p, s)
    
    

def removeChildren(v, c, s):
    if v not in c:
        if v in s: 
            s.remove(v)
        return

    for x in c[v]:
        if x in s:
            s.remove(x)
        removeChildren(x, c, s)
    


            
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

suspect = range(1, n+1)

victim = int(raw_input())
while (victim != ""):
    victim = int(victim)
    removeParents(victim, parents, suspect)
    removeChildren(victim, children, suspect)
    if victim in suspect:
        suspect.remove(victim)
    try:
        victim = raw_input()
    except EOFError:
        victim = ""


if len(suspect) == 0:
    print "0"
else:
    print ' '.join(map(str, suspect))

