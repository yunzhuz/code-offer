class treenode():
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class solution():
    def rebuilt(self,pre,mid):
        # print(pre)
        if len(pre)>0:
            root=treenode(pre[0])
            rootid=mid.index(root.val)     ##要求序列中不能有重复的数字
            root.left=self.rebuilt(pre[1:1+rootid],mid[:rootid])
            root.right=self.rebuilt(pre[1+rootid:],mid[1+rootid:])

            return root

    # def preorder(self,treenode):
    #     if treenode == None:
    #         return
    #     a=[]
    #     while treenode !=None or a:
    #         while treenode!=None:
    #             print(treenode.val)
    #             a.append(treenode)
    #             treenode=treenode.left
    #         if a:
    #             treenode=a.pop().right
    #     print()

    def preorder1(self,treenode):
        if treenode == None:
            return
        else:
            print(treenode.val)
            self.preorder1(treenode.left)
            self.preorder1(treenode.right)

    def midorder(self,treenode):
        if treenode == None:
            return
        else:
            self.midorder(treenode.left)
            print(treenode.val)
            self.midorder(treenode.right)

    def endorder(self,treenode):
        if treenode ==None:
            return
        else:
            self.endorder(treenode.left)
            self.endorder(treenode.right)
            print(treenode.val)


if __name__=='__main__':
    pre=[1,2,4,7,3,5,6,8]
    mid=[4,7,2,1,5,3,8,6]
    tree=solution().rebuilt(pre,mid)
    # solution().preorder(tree)
    solution().preorder1(tree)
    print('=============')
    solution().midorder(tree)
    print('=============')
    solution().endorder(tree)
      