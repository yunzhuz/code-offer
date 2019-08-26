class solution():
    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def insert(self,data):
        self.queue1.insert(0,data)

    def deletefromtop(self):
        # print(self.queue1)
        if not self.queue1:
            return
        
        while len(self.queue1)!=1:
            self.queue2.insert(0,self.queue1.pop())
        # print(self.queue2)
        a=self.queue1
        self.queue1=self.queue2 
        self.queue2=[]
        return a.pop()

if __name__ == '__main__':
    a = solution()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    print(a.deletefromtop())
    print(a.deletefromtop())
    a.insert(4)
    print(a.deletefromtop())
    

    