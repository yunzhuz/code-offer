class solution():
    def __init__(self):
         self.stack1=[]
         self.stack2=[]

    def appendtail(self,data):
        self.stack1.append(data)
        return self.stack1

    def deleteHead(self):
        print(self.stack1)
        # print(self.stack2)
        if not self.stack1 and not self.stack2:
            print('---')
            return
        if not self.stack2:     #如果stack2为空
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == '__main__':
    a=solution()
    a.appendtail(1)
    a.appendtail(2)
    a.appendtail(3)
    a.appendtail(4)
    print(a.deleteHead())
    print(a.deleteHead())
    a.appendtail(5)
    a.appendtail(6)
    print(a.deleteHead())
    print(a.deleteHead())
    print(a.deleteHead())
    print(a.deleteHead())


