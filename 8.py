class treenode():
    def __init__(self,data,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent

class solution():
    def midorder(self,treenode):
        if treenode ==None:
            return
        else:
            
            self.midorder(treenode.left)
            print(treenode.data)
            self.midorder(treenode.right)


    def findnext(self,treenode):
        if treenode==None:
            return
        if treenode.right!=None:
            node=treenode.right
            while node.left!=None:
                node=node.left
            return node
        elif treenode==treenode.parent.left:
            return treenode.parent
        else:
            while treenode.parent.parent!=None and treenode.parent==treenode.parent.parent.right:
                treenode=treenode.parent
            if treenode.parent.parent==None:
                print('no next')
                return
            return treenode.parent.parent

if __name__ == '__main__':
    n9 = treenode('h')
    n8 = treenode('i')
    n7 = treenode('e',left=n9,right=n8)
    n6 = treenode('d')
    n5 = treenode('f')
    n4 = treenode('g')
    n3 = treenode('b',left=n6,right=n7)
    n2 = treenode('c',left=n5,right=n4)
    n1 = treenode('a',left=n3,right=n2)
    n2.parent = n1
    n3.parent = n1
    n4.parent = n2
    n5.parent = n2
    n6.parent = n3
    n7.parent = n3
    n8.parent = n7
    n9.parent = n7
    solution().midorder(n1)
    print('=========')
    x=solution().findnext(n4).data
    print(x)


