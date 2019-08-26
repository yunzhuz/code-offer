class listnode:
    def __init__(self,x):
        self.data=x
        self.next=None

class f():
    def __init__(self):
        self.head = None
        
    def makelist(self,data):
        self.head = listnode(data[0])
        p = self.head
        for i in data[1:]:
            node=listnode(i)
            p.next=node
            p=p.next
        return self.head

    def solution(self,head):
        p = head
        l = []
        while p != None:
            l.append(p.data)
            p = p.next
        n = len(l)
        if n%2 == 0:
            mid = n//2
            a = l[0:mid]
            b = l[mid:n]
            b = b[::-1]
            result = []
            for i in range(len(b)):
                result.append(a[i])
                result.append(b[i]) 
            return self.makelist(result)
        else:
            mid = n//2 +1
            a = l[0:mid]
            b = l[mid:n]
            b = b[::-1]
            result = []
            for i in range(len(b)):
                result.append(a[i])
                result.append(b[i])
            result.append(a[len(b)])
            return self.makelist(result)

l = f()
p = l.makelist([1,2,3,4,5])
print(f().solution(p).next.data)