class treenode():
    def __init__(self,data,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent

class solution():
    def preorder(self,treenode):
        if treenode==None:
            return
        else:
            print(treenode.data)
            self.preorder(treenode.left)
            self.preorder(treenode.right)
        
if __name__ == '__main__':
    n8=treenode('8')
    n7=treenode('7')
    n6=treenode('6',left=n8)
    n5=treenode('5')
    n4=treenode('4',right=n7)
    n3=treenode('3',left=n5,right=n6)
    n2=treenode('2',left=n4)
    n1=treenode('1',left=n2,right=n3)
    n2.parent=n1
    n3.parent=n1
    n4.parent=n2
    n5.parent=n3
    n6.parent=n3
    n7.parent=n4
    n8.parent=n6
    solution().preorder(n1)

