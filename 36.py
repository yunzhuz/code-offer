class treenode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def solution(node):
    l = []
    midorder(node,l)
    n = len(l)
    for i in range(n-1):
        l[i].right = l[i+1]
        l[i+1].left = l[i]
    return l[0]

def midorder(node,l):
    if not node:
        return
    else:
        midorder(node.left,l)
        l.append(node)
        midorder(node.right,l)

if __name__ == '__main__':
    n1 = treenode(10)
    n2 = treenode(6)
    n3 = treenode(14)
    n4 = treenode(4)
    n5 = treenode(8)
    n6 = treenode(12)
    n7 = treenode(16)
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n3.left , n3.right = n6 , n7
    a = solution(n1)
    print(a.right.right.right.right.left.left.data)