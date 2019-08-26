class treenode():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def mirror(node):
    if node:
        node.left , node.right = node.right , node.left
        mirror(node.left)
        mirror(node.right)
    return node

def preorder(node):
    if node:                
        print(node.data)
        preorder(node.left)
        preorder(node.right)
    

if __name__ == '__main__':
    n1 = treenode(8)
    n2 = treenode(6)
    n3 = treenode(10)
    n4 = treenode(5)
    n5 = treenode(7)
    n6 = treenode(9)
    # n7 = treenode(11)
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n3.left = n6
    # n3.left , n3.right = n6 , n7
    n = mirror(n1)
    preorder(n)