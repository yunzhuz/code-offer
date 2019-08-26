class node():
    def __init__(self,data):
        self.data = data
        self.next = None

###方法1
def merge(head1,head2):
    p1 = head1
    p2 = head2
    l = []
    while p1 != None:
        l.append(p1.data)
        p1 = p1.next
    while p2 != None:
        l.append(p2.data)
        p2 = p2.next
    l = sorted(l)
    nhead = node(l[0])
    np = nhead
    for i in l[1:]:
        np.next = node(i)
        np = np.next
    return nhead

def solution(head1,head2):
    if head1 == None and head2 == None:
        return None
    if head1 == None and head2 != None:
        return head2
    if head2 == None and head1 != None:
        return head1
    nhead = None
    p1 , p2 = head1 , head2
    if p1.data < p2.data:
        nhead = p1
        if p1.next!= None:
            paixu(nhead,p1.next,p2)
        else:
            nhead.next = p2
    else:
        nhead = p2
        if p2.next != None:
            paixu(nhead,p1,p2.next)
        else:
            nhead.next = p2
    return nhead

def paixu(p,p1,p2):
    if p1.data < p2.data:
        p.next = p1
        if p1.next != None:
            paixu(p.next,p1.next,p2)
        else:
            p1.next = p2
    else:
        p.next = p2
        if p2.next != None:
            paixu(p.next,p1,p2.next)
        else:
            p2.next = p1

if __name__ == '__main__':
    n1 = node(1)
    n2 = node(3)
    n3 = node(5)
    n4 = node(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    nn1 = node(2)
    nn2 = node(4)
    nn3 = node(6)
    nn4 = node(8)
    nn1.next = nn2
    nn2.next = nn3
    nn3.next = nn4
    print(solution(n1,nn1).next.next.next.data)