class treenode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def solution(root,count):
    path = []
    currentsum = 0
    findpath(root,path,currentsum,count)

def findpath(node,path,currentsum,count):
    path.append(node)
    currentsum += node.data
    if currentsum == count and node.left == None and node.right == None:
        for i in path:
            print(i.data,end=' ')
        print()
    if node.left:
        findpath(node.left,path,currentsum,count)
    if node.right:
        findpath(node.right,path,currentsum,count)
    path.pop()


if __name__ == '__main__':
    n1 = treenode(10)
    n2 = treenode(5)
    n3 = treenode(12)
    n4 = treenode(4)
    n5 = treenode(7)
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5 
    solution(n1,22) 