class node():
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    p = head
    l = []
    while p != None:
        l.append(p.data)
        p = p.next
    l = l[::-1]
    nhead = node(l[0])
    np = nhead
    for i in l[1:]:
        np.next = node(i)
        np = np.next
    return nhead


if __name__ == '__main__':
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)
    n5 = node(5)
    n6 = node(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    print(reverse(n1).next.next.data)