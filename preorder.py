'''
@author: Austin Walters
@language: Python 2.7
@date: 9/28/2014
@description: Various Traversals For Trees
'''
import Queue

'''
A classic node class for use in a tree
'''
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

'''
Creates a general Binary Tree
'''
class BinaryTree(Node):
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            root = Node(data)
        else:
            if(data <= root.data):
               root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)
        return root

    '''
    In Order Traversal of the tree
    '''
    def InOrder(self, root):
        if root is None:
            pass
        else:
            self.InOrder(root.left)
            print(root.data),
            self.InOrder(root.right)

    '''
    Pre Order Traversal of the tree
    '''
    def PreOrder(self, root):
        if root is None:
            pass
        else:
            print(root.data),
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    '''
    Post Order Traversal
    '''
    def PostOrder(self, root):
        if root is None:
            pass
        else:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data),

    
    '''
    Level Order Traversal
    '''
    def LevelOrder(self, root):
        if root is None:
            pass
        else:
            q = Queue.Queue()
            currLevelCount = 1
            nextLevelCount = 0
            q.put(root)
            while not q.empty():
                root = q.get()
                currLevelCount -= 1
                if root is not None:
                    print(root.data),
                    q.put(root.left)
                    q.put(root.right)
                    nextLevelCount += 2
                if currLevelCount is 0:
                    print ""
                    currLevelCount = nextLevelCount
                    nextLevelCount = 0


'''
Generates a binary tree to play with
'''
bint = BinaryTree()
root = bint.insert(None, 40)
bint.insert(root,4)
bint.insert(root,34)
bint.insert(root,45)
bint.insert(root,14)
bint.insert(root,55)
bint.insert(root,48)

print "\n\nPre Order Traversal:"
bint.PreOrder(root)
print "\n\nIn Order Traversal:"
bint.InOrder(root)
print "\n\nPost Order Traversal:"
bint.PostOrder(root)
print "\n\nLevel Order Traversal:"
bint.LevelOrder(root)

