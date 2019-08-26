class listnode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def deletenode(head,node):
    if node.next != None:
        node.data = node.next.data
        node.next = node.next.next
    if head.next == None:
        return
    else:
        p = head
        while p.next != node:
            p = p.next
        p.next = None
    return head

def deleterepeat(head):
    p = head
    newhead = listnode(00)
    newhead.next = head
    np = newhead
    while p and p.next:
        if p.data != p.next.data:
            p = p.next
            np = np.next
        else:
            val = p.data
            while p.data == val:
                p = p.next
            np.next = p
    return newhead.next

def deleterepeat1(head):
    p = head
    while p and p.next:
        if p.data != p.next.data:
            None
        else:
            nextnode = p.next
            while nextnode.data == nextnode.next.data:
                nextnode = nextnode.next
            p.next = nextnode.next
        p = p.next
    return head
                
n1 = listnode(1)
n2 = listnode(2)
n3 = listnode(3)
n4 = listnode(2)
n5 = listnode(3)
n6 = listnode(3)
n7 = listnode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
np = deleterepeat1(n1)
while np:
    print(np.data)
    np = np.next