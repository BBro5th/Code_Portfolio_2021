# Day 17 exercise (due next Monday at 8am, have a good thanksgiving!)

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

# Sample code to build a tree with 3 nodes
# r = BinaryTree('a')
# r.insertLeft('b')
# r.insertRight('c')

# Sample code to use 3 different traversals to visit all the nodes in the tree
# print("-----preorder:")
# r.preorder()
# print("-----postorder:")
# r.postorder()
# print("-----inorder:")
# r.inorder()

Alfa= BinaryTree("A")
Alfa.insertRight("AB")
Alfa.insertLeft("AC")
# exercise pt 1
Def=BinaryTree("Aroot")
Def.insertLeft("left")
Def.insertRight("right")
Def.leftChild.insertLeft("Lleft")
Def.leftChild.insertRight("Lright")
print("preorder______")
Def.preorder()
print("postorder_____")
Def.postorder()
print("inorder______")
Def.inorder()

#CEK=BinaryTree("root")
#CEK.insertLeft("kinder")
#CEK.insertRight(Alfa)
# print("preorder______")
# Alfa.postorder()
# print("postorder_____")
# Alfa.preorder()
# print("inorder______")
# Alfa.inorder()
# print("--preorder______")
# CEK.postorder()
# print("--postorder_____")
# CEK.preorder()
# print("--inorder______")
# CEK.inorder()

#exercise pt 2
EX2=BinaryTree("Book")
EX2.insertLeft("Chapter 1")
EX2.insertRight("Chapter2")
EX2.leftChild.insertLeft("Section 1.1")
EX2.leftChild.insertRight("Section 1.2")
EX2.leftChild.rightChild.insertLeft("Section 1.2.1")
EX2.leftChild.rightChild.insertRight("Section 1.2.2")
EX2.rightChild.insertLeft("Section 2.1")
EX2.rightChild.insertRight("Section 2.2")
EX2.rightChild.rightChild.insertRight("Section 2.2.2")
EX2.rightChild.rightChild.insertLeft("Section 2.2.1")

print("--preorder______")
EX2.preorder()
print("--postorder_____")
EX2.postorder()
print("--inorder______")
EX2.inorder()