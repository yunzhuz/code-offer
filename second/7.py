class treenode():
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

def solution(l1,l2):
    if len(l1) > 0:
        node = treenode(l1[0])
        nodeid = l2.index(l1[0])
        node.left = solution(l1[1:1+nodeid],l2[:nodeid])
        node.right = solution(l1[1+nodeid:],l2[1+nodeid:])
        return node

def preorder(node):
    if not node:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

l1 = [1,2,4,7,3,5,6,8]
l2 = [4,7,2,1,5,3,8,6]
head = solution(l1,l2)
preorder(head)
