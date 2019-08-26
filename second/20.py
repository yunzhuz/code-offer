def solution(s):
    try:
        s = float(s)
        print(s)
    except:
        print('false')


class f():
    def solution2(self,s):
        if len(s) == 0:
            return False
        s = s.lower()
        count = s.count('e')
        if count > 1:
            return False
        if count == 1:
            index = s.index('e')
            left = s[:index]
            right = s[index+1:]
            if '.' in right or len(right) == 0:
                return False
            isfleft = self.isleft(left)
            isright = self.isright(right)
            return isfleft and isright
        else:
            return self.isleft(s)
    def isleft(self,s):
        allstring = ['0','1','2','3','4','5','6','7','8','9','+','-','.']
        dotcount = 0
        for i in range(len(s)):
            if s[i] not in allstring:
                return False
            if s[i] == '.':
                dotcount += 1
            if (s[i] == '+' and i != 0) or (s[i] == '-' and i!=0):
                return False
        if dotcount > 1:
            return False
        return True
    def isright(self,s):  ##指数部分必须为整数
        allstring = ['0','1','2','3','4','5','6','7','8','9','+','-']
        for i in range(len(s)):
            if s[i] not in allstring:
                return False
            if (s[i] == '+' and i != 0) or (s[i] == '-' and i!=0):
                return False
        return True
            

s = '.123'
print(f().solution2(s))