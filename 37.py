class treenode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def xuliehua(node,l):
    if not node:
        l.append('$')
        return
    else:
        l.append(node.data)
        xuliehua(node.left,l)
        xuliehua(node.right,l)

def fanxuliehua(l,i):
    if i >= len(l) or l[i] == '$':
        return None,i+1
    node = treenode(l[i])
    i += 1
    node.left , i = fanxuliehua(l,i)
    node.right , i = fanxuliehua(l,i)
    return node , i

def preorder(node):
    if not node:
        return
    else:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

if __name__ == '__main__':
    n1 = treenode(1)
    n2 = treenode(2)
    n3 = treenode(3)
    n4 = treenode(4)
    n5 = treenode(5)
    n6 = treenode(6)
    n1.left , n1.right = n2 , n3
    n2.left = n4
    n3.left , n3.right = n5 , n6
    l = []
    xuliehua(n1,l)
    print(l)
    n,i= fanxuliehua(l,0)
    print(i)
    preorder(n)