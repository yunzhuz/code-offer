class stack:
    def __init__(self):
        self.s = []
        self.m = []
    
    def push(self,data):
        self.s.append(data)
        if len(self.m) ==0 or data < self.m[-1]:
            self.m.append(data)
        else:
            self.m.append(self.m[-1])     ##每次添加元素时都对最小元素栈也添加元素是为了进行pop操作的时候，也能将最小栈进行删除操作
    
    def pop(self):
        self.s.pop()
        self.m.pop()
    
    def min(self):
        print(self.m[-1])

if __name__ == '__main__':
    a = stack()
    a.push(3)
    a.push(2)
    a.min()
    a.pop()
    a.min()
    a.push(2)
    a.push(4)
    a.min()