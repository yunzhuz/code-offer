class treenode():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def depth(node):
    if not node:
        return 0
    ldepth = depth(node.left)
    rdepth = depth(node.right)
    return max(ldepth,rdepth) + 1

##题目2
def solution1(node):
    if not node:
        return True
    left = depth(node.left)
    right = depth(node.right)
    if abs(left - right) > 1:
        return False
    return solution1(node.left) and solution1(node.right)

def solution2(node):
    d = [0]
    return isbalance(node,d)

def isbalance(node,d):
    if not node:
        d = [0]
        return True
    left = [0]
    right = [0]
    if isbalance(node.left,left)  and isbalance(node.right,right):
        dif = abs(left[0] - right[0])
        if dif <= 1:
            d[0] = max(left[0],right[0]) + 1
            return True
    return False


if __name__ == '__main__':
    n1 = treenode(1)
    n2 = treenode(2)
    n3 = treenode(3)
    n4 = treenode(4)
    n5 = treenode(5) 
    n6 = treenode(6)
    n7 = treenode(7)
    n8 = treenode(8)

    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n3.right = n6
    n5.left = n7
    n7.left = n8
    print(depth(n1))
    print(solution2(n1))