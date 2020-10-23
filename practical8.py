# 8. Write a program for inorder, postorder and preorder traversal of tree.

class Node:
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
    def insert(self, data):
        
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
                
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()
            
    def printPreOrder(self):
        if self.val:
            print(self.val)
            
            if self.left:
                self.left.printPreOrder()

            if self.right:
                self.right.printPreOrder()
            
    def printInOrder(self):
        if self.val:
            
            if self.left:
                self.left.printInOrder()
            print(self.val)
            if self.right:
                self.right.printInOrder()
            
    def printPostOrder(self):
        if self.val:
            
            if self.left:
                self.left.printPostOrder()
        
            if self.right:
                self.right.printPostOrder()
            print(self.val)
            
            
        
                
# root = Node(10)
# root.left = Node(12)
# root.right = Node(5)
# root.printTree()

print("After Insert")
root1= Node(None)
root1.insert(20)
root1.insert(4)
root1.insert(13)
root1.insert(130)
root1.insert(130)
root1.insert(123)
root1.printTree()

print("Inorder")
root1.printInOrder()

print("Postorder")
root1.printPostOrder()

print("Preorder")
root1.printPreOrder()
