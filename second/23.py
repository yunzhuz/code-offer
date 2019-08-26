class node():
    def __init__(self,data):
        self.data = data
        self.next = None

def xunzhao(head):
    if not head.next or not head.next.next:
        return None
    meetingnode = panduan(head)
    if meetingnode == None:
        return None
    pcount = meetingnode.next
    count = 1
    while pcount != meetingnode:
        pcount = pcount.next
        count +=1
    p1 = head
    p2 = meetingnode
    for i in range(count):
        p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def panduan(head):
    pslow = head.next
    pfast = head.next.next
    while pfast and pfast.next != None and pfast != pslow:
        pslow = pslow.next
        pfast = pfast.next.next
    if not pfast:
        return None
    return pfast


###  方法2  不用统计环中节点个数
class Solution:
    def EntryNodeOfLoop(self, head):
        if not head.next or not head.next.next:
            return None
        p1 = head
        p2 = self.panduan(head)
        if not p2:
            return None
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    def panduan(self,head):
        pslow = head.next
        pfast = head.next.next
        while pfast and pfast.next != None and pfast != pslow:
            pslow = pslow.next
            pfast = pfast.next.next
        if not pfast or not pfast.next:
            return None
        return pfast

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
    n6.next = n3
    print(xunzhao(n1).data)