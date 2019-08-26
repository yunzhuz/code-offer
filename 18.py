class listnode():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def deletenode(head,node):
    if node.next != None:
        node.data = node.next.data
        node.next = node.next.next
    elif head.next == None:
        return
    else:
        p = head
        while p.next != node:
            p = p.next
        p.next = None
    return head

##题目二
def deleterepeat(head):   ##方法1  只适用于去除连续的重复元素 满足题目给出的列表的要求
    p = head
    newhead = listnode(-1)
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

def deleterepeat1(head):    ##方法2   适用于即使重复元素不是连续的
    p = head
    l = []
    while p:
        l.append(p.data)
        p = p.next
    l = list(filter(lambda x:l.count(x)==1,l))    ##filter函数 去除不满足条件的元素
    print(l)
    newhead = listnode(l[0])
    np = newhead
    for i in l[1:]:
        np.next = listnode(i)
        np = np.next
    return newhead

##题目二扩展   删除重复元素 保存一次
def deleterepeat2(head):
    p = head
    while p and p.next:
        if p.data != p.next.data:
            None
        else:
            next = p.next
            while  next.data == p.data: 
                next = next.next
            p.next = next
        p = p.next
    return head

def deleterepeat3(head):
    p = head
    l = []
    while p:
        if p.data not in l:
            l.append(p.data)
        p = p.next
    newhead = listnode(l[0])
    np = newhead
    for i in l[1:]:
        np.next = listnode(i)
        np = np.next
    return newhead


#题目一
# n1 = listnode(1)
# n2 = listnode(2)
# n3 = listnode(3)
# n4 = listnode(4)
# n5 = listnode(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# # print(n2.next.next.data)
# p=deletenode(n1,n4)
# while p != None:
#     print(p.data)
#     p = p.next


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
# print(n2.next.next.data)
p=deleterepeat2(n1)
while p != None:
    print(p.data)
    p = p.next
