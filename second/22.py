class listnode():
    def __init__(self,data):
        self.data = data
        self.next = None

def solution(head,k):
    p = head
    count = 0
    while p:
        count += 1
        p = p.next
    np = head
    if k > count:
        return False
    else:
        index = count - k
        j = 0
        while np and j < index:
            np = np.next
            j += 1
        print(np.data)

n1 = listnode(1)
n2 = listnode(2)
n3 = listnode(3)
n4 = listnode(4)
n5 = listnode(5)
n6 = listnode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
solution(n1,6)