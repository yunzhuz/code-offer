class treenode():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def midorder(node,l):
    if node == None:
        return
    else:
        midorder(node.left,l)
        l.append(node)
        midorder(node.right,l)

def solution(node,k):
    l = []
    midorder(node,l)
    return l[k-1].data


if __name__ == '__main__':
    n1 = treenode(5)
    n2 = treenode(3)
    n3 = treenode(7)
    n4 = treenode(2)
    n5 = treenode(4)
    n6 = treenode(6)
    n7 = treenode(8)

    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n3.left , n3.right = n6 , n7
    print(solution(n1,3))