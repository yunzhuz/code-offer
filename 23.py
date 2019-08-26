class node():
    def __init__(self,data):
        self.data = data
        self.next = None

def panduan(head):
    if not isinstance(head,node) or not head:
        return None
    pslow = head.next     ###这里不能把两个指针都指到头指针，否则下面的循环判断两个指针是否相遇将永远正确，停留在头指针上
    pfast = head.next.next
    while pfast and pfast.next != None and pfast != pslow:
        pslow = pslow.next
        pfast = pfast.next.next
    if not pfast or not pfast.next:
        return None
    return pfast

def xunzhao(head):
    if not isinstance(head,node) or not head:
        return None
    meetingnode = panduan(head)
    if not meetingnode:
        return None
    p1 = head
    p2 = meetingnode  ##第一次相遇的指针和头指针以相同的速度后移，当两个指针再次相遇时的节点即为环的入口节点
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
    


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
    print(xunzhao(n1).data)
    