class listnode:
    def __init__(self,x):
        self.data=x
        self.next=0

class linklist():
    def __init__(self):
        self.head = 0

    def makelist(self,data):
        self.head=listnode(data[0])
        p=self.head

        for i in data[1:]:
            node=listnode(i)
            p.next=node
            p=p.next

    def getitem(self,index):

        j=0
        p=self.head

        while p.next!=0 and j<index:
            p=p.next
            j+=1

        if j==index:
            return p.data

        else:
            print('target is not exit')
    
    def printfromend(self):
        p=self.head
        a=[ ]
        while p.next !=0:
            a.append(p.data)
            p=p.next
        a.append(p.data)
        return a[::-1]
        # return ''.join(a[::-1])

l = linklist()
l.makelist([1,2,3,4,5])
print(l.getitem(5))
print(l.printfromend())