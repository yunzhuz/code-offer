class listnode():
    def __init__(self,data):
        self.data = data
        self.next = None

def solution(head):
    p = head
    l = []
    while p:
        l.append(p.data)
        p = p.next
    l = l[::-1]
    nhead = listnode(l[0])
    np = nhead
    for i in l[1:]:
        node = listnode(i)
        np.next = node
        np = np.next
    return nhead

###主要方法   运算快
def solution1(head):
    nhead = None
    p = head
    pp = None
    while p:
        pnext = p.next
        if p.next == None:
            nhead = p
        p.next = pp
        pp = p
        p = pnext
    return nhead

if __name__ == '__main__':
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
    print(solution1(n1).next.next.data)