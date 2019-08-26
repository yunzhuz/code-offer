class treenode():
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if not node:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

if __name__ == "__main__":
    n1 = treenode(1)
    n2 = treenode(2)
    n3 = treenode(3)
    n4 = treenode(4)
    n5 = treenode(5)
    n6 = treenode(6)
    n7 = treenode(7)
    n8 = treenode(8)
    n1.left , n1.right = n2 , n3
    n2.left = n4
    n3.left , n3.right = n5 , n6
    n4.right = n7
    n6.left = n8

    preorder(n1)