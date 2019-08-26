class listnode():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def solution(p):
    l = []
    l.append(p.data)
    while p.next:
        l.append(p.next.data)
        p = p.next
    l = l[::-1]
    nhead = listnode(l[0])
    np = nhead
    for i in l[1:]:
        node = listnode(i)
        np.next = node
        np = np.next
    return nhead

if __name__ == '__main__':
    l = [1,2,3,4,5]
    head = listnode(l[0])
    p = head
    for i in l[1:]:
        node = listnode(i)
        p.next = node
        p = p.next
    print(solution(head).next.data)