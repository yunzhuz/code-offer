class solution():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self,data):
        self.s1.append(data)
        if len(self.s2) == 0 or data < self.s2[-1]:
            self.s2.append(data)
        else:
            self.s2.append(self.m[-1])

    def pop(self):
        self.s1.pop()
        self.s2.pop()

    def min(self):
        print(self.s2[-1])