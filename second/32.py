class treenode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def solution(root):     ###不分行从上到下打印二叉树
    if not isinstance(root,treenode):
        return None
    l = []
    l.append(root)
    while len(l) > 0:
        temp = l.pop(0)
        print(temp.data,end=' ')
        if temp.left:
            l.append(temp.left)
        if temp.right:
            l.append(temp.right)

def solution2(root):     ###分行从上到下打印二叉树
    if not isinstance(root,treenode):
        return None
    l = []
    tobeprint ,nextprin = 1 , 0
    l.append(root)
    while len(l) > 0:
        temp = l.pop(0)
        print(temp.data , end = ' ')
        tobeprint -= 1
        if temp.left:
            l.append(temp.left)
            nextprin += 1
        if temp.right:
            l.append(temp.right)
            nextprin += 1
        if tobeprint == 0:
            print()
            tobeprint = nextprin
            nextprin = 0

def solution3(root):     ##之字形打印二叉树
    l1 = []
    l1.append(root)
    l2 = []
    s = [l1,l2]
    level = 1
    tobeprint , nextprin = 1 , 0
    while len(s[0])>0 or len(s[1])>0:
        a = (level + 1)%2
        l = s[a]
        temp = l.pop()
        print(temp.data,end=' ')
        tobeprint -= 1
        if a == 0:
            if temp.left:
                s[1].append(temp.left)
                nextprin += 1
            if temp.right:
                s[1].append(temp.right)
                nextprin += 1
        else:
            if temp.right:
                s[0].append(temp.right)
                nextprin += 1
            if temp.left:
                s[0].append(temp.left)
                nextprin += 1
        if tobeprint == 0:
            print()
            level += 1
            tobeprint = nextprin
            nextprin = 0



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