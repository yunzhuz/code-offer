class treenode():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def solution(node1,node2):
    if not isinstance(node1,treenode) or not isinstance(node2,treenode):
        return False
    result = False
    if node1 and node2:
        if node1.data == node2.data:                 ##先遍历大树找到相同的节点，然后在判断左右子节点是否相同
            result = judge(node1 , node2)
        if not result:
            result = solution(node1.left , node2)
        if not result:
            result = solution(node1.right , node2)
    return result

def judge(node1,node2):
    if not node2:
        return True
    if not node1:
        return False
    if node1.data != node2.data:
        return False
    return judge(node1.left , node2.left) and judge(node1.right , node2.right)

if __name__ == '__main__':
    n1 = treenode(8)
    n2 = treenode(8)
    n3 = treenode(7)
    n4 = treenode(9)
    n5 = treenode(2)
    n6 = treenode(4)
    n7 = treenode(7)
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    n5.left , n5.right = n6 , n7
    nn1 = treenode(8)
    nn2 = treenode(9)
    nn3 = treenode(3)
    nn1.left , nn1.right = nn2 , nn3
    print(solution(n1,nn1))