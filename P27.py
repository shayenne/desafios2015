#!/usr/bin/env python

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
	if tree != None:
		printTree(tree.getLeftChild())
		print(tree.getNodeValue())
		printTree(tree.getRightChild())



# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)	

#testTree()
n = int(raw_input())

first = map(int, raw_input().split())
tree = BinaryTree(first)

for i in range(n-1):
	[x, y] = map(int, raw_input().split())
	parent = tree
	val = parent.getNodeValue()
	child = parent
	
	while child != None and (val[0] < x or val[1] < y): 
		tmp = child
		child = parent.getLeftChild()
		parent = tmp
		val = parent.getNodeValue()
	"""	
	if val[0] >= x and val[1] >= y:
		parent.insertRight([x, y])
	else:
		parent.insertLeft([x, y])
	"""
	if child == None:
		parent.insertLeft([x, y])
	else:
		parent.insertRight
	
printTree(tree)
