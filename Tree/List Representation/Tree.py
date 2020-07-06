from typing import Any

def BinaryTree(r):
    return [r, [], []]

def insertLeft(r: list,  newBranch: Any):
    t = r.pop(1)
    r.insert(1, [newBranch, t, []])

def insertRight(r:list, newBranch: Any):
    t = r.pop(2)
    r.insert(2, [newBranch, [], t])

def getRootVal(root: list):
    return root[0]

def setRootVal(root: list,newVal: Any):
    root[0] = newVal

def getLeftChild(root: list):
    return root[1]

def getRightChild(root: list):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
print(r)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))