class treenode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def solution(node):   ##不分行从上到下打印二叉树
    l = []
    l.append(node)
    #print(l)                                                    
    while len(l) > 0:
        temp = l.pop(0)
        print(temp.data , end=' ')
        if temp.left:
            l.append(temp.left)
        if temp.right:
            l.append(temp.right)

def solution2(node):  ##分行从上到下打印二叉树
    l = []
    l.append(node)
    tobeprint , nextlevel = 1 , 0
    while len(l) > 0:
        temp = l.pop(0)
        print(temp.data , end=' ')
        tobeprint -= 1
        if temp.left:
            nextlevel += 1
            l.append(temp.left)
        if temp.right:
            nextlevel += 1
            l.append(temp.right)
        if tobeprint == 0:
            print()
            tobeprint = nextlevel
            nextlevel = 0

def solution3(node):  ##之字形打印二叉树
    l = []
    l.append(node)
    m = []
    s = [l,m]
    current , nextlevel = 0 , 1
    while len(l) > 0 or len(m) > 0:
        temp = s[current].pop()
        print(temp.data , end=' ')
        if current == 0:
            if temp.left:
                s[nextlevel].append(temp.left)
            if temp.right:
                s[nextlevel].append(temp.right)
        else:
            if temp.right:
                s[nextlevel].append(temp.right)
            if temp.left:
                s[nextlevel].append(temp.left)
        if len(s[current]) == 0:
            print()
            current = 1 - current
            nextlevel = 1 - nextlevel



if __name__ == '__main__':
    n1 = treenode(8)
    n2 = treenode(6)
    n3 = treenode(10)
    n4 = treenode(5)
    n5 = treenode(7)
    n6 = treenode(9)
    n7 = treenode(11)
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n3.left , n3.right = n6 , n7                                                                                                                                                                                                                                                                                                                                                                         

    solution3(n1)