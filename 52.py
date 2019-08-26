class listnode():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def solution1(head1,head2): ##暴力法，遍历链表a，同时查看链表b中是否有该节点
    p1 = head1
    while p1:
        a = p1.data
        p2 = head2
        while p2:
            b = p2.data
            if p1 == p2:
                return p1.data
            else:
                p2 = p2.next
        p1 = p1.next

def solution2(head1,head2):
    if not head1 or not head2:
        return
    if not isinstance(head1,listnode) or not isinstance(head2,listnode):
        return
    l1 , l2 = [] ,[]
    p1 , p2 = head1 , head2
    while p1:
        l1.append(p1)
        p1 = p1.next
    while p2:
        l2.append(p2)
        p2 = p2.next
    a , b = l1.pop() , l2.pop()
    while l1 and l2 and a == b:     ##将两个链表分别放入两个列表中，尾部的元素相同，从尾部算，第一个不同的节点的下一个节点即为所求
        a , b = l1.pop() , l2.pop()
    return a.next.data

def solution3(head1,head2):
    p1 , p2 = head1 , head2
    n1 ,n2 = 0 ,0
    while p1:
        n1 += 1
        p1 = p1.next
    while p2:
        n2 += 1
        p2 = p2.next
    dis = abs(n1 - n2)
    p1 , p2 = head1 , head2
    if n1 < n2:
        p1 , p2 = head2 , head1
    for i in range(dis):
        p1 = p1.next
    while p1 and p2 and p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1.data
    



if __name__ == '__main__':
    n1 = listnode(1)
    n2 = listnode(2)
    n3 = listnode(3)
    n4 = listnode(4)
    n5 = listnode(5)
    n6 = listnode(6)
    n7 = listnode(7)

    n1.next = n2
    n2.next = n3
    n3.next = n6
    n4.next = n5
    n5.next = n6
    n6.next = n7
    print(solution3(n1,n4))