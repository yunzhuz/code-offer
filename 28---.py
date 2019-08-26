class treenode():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def solution(node1,node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.data != node2.data:
        return False
    return solution(node1.left , node2.right) and solution(node1.right , node2.left) ##所有返回值均为true时最后的返回才为true
    

if __name__ == '__main__':
    n1 = treenode(8)
    n2 = treenode(6)
    n3 = treenode(6)
    n4 = treenode(5)
    n5 = treenode(7)
    n6 = treenode(7)
    n7 = treenode(5)
    n1.left , n1.right = n2 , n3
    n2.left , n2.right = n4 , n5
    #n3.left , n3.right = n6 , n7
    n3.left = n6
    print(solution(n1,n1))