class listnode():
    def __init__(self,data):
        self.data = data
        self.next = None

class function():
    def __init__(self):
        self.head = None

    def makelist(self,array):
        self.head = listnode(array[0])
        p = self.head
        for i in array[1:]:
            p.next = listnode(i)
            p = p.next

    def getitem(self,index):
        if index == 0:
            return
        else:
            j = 1
            p = self.head
            count = 1
            while p.next != None:
                p = p.next
                count += 1
            th = count - index + 1
            print(th)
            np = self.head
            while np.next != None and j < th:
                np = np.next
                j += 1
            if j == th:
                return np.data
            else:
                print('no target')

l = function()
l.makelist([1,2,3,4,5,6])
print(l.getitem(1))

