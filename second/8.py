class treenode():
    def __init__(self,data,left = None,right = None,parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def solution(node):
    if not node :
        return
    if node.right != None:
        node = node.right
        while node.left != None:
            node = node.left
        return node
    elif node == node.parent.left:
        return node.parent
    else:
        while node.parent.parent != None and node.parent == node.parent.parent.right:
            node = node.parent
        if node.parent.parent = None:
            print('no next')
            return
        return node.parent.parent

if __name__ == '__main__':
    n1 = treenode('a')
    n2 = treenode('b')
    n3 = treenode('c')
    n4 = treenode('d')
    n5 = treenode('e')
    n6 = treenode('f')
    n7 = treenode('g')
    n8 = treenode('h')
    n9 = treenode('i')
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n3.left , n3.right = n6 , n7
    n5.left , n5.right = n8 , n9
    n2.parent = n1
    n3.parent = n1
    n4.parent = n2
    n5.parent = n2
    n6.parent = n3
    n7.parent = n3
    n8.parent = n7
    n9.parent = n7

    solution(n3)
    