# 递归的思路就是n位gray码是由n-1位gray码生成，举个例子简单一些：
# 比如求n=3的gray码，首先知道n=2的gray码是(00,01,11,10)
# 那么n=3的gray码其实就是对n=2的gray码首位添加0或1生成的，添加0后变成(000,001,011,010)
# 添加1后需要顺序反向就变成(110,111,101,100)
# 组合在一起就是(000,001,011,010,110,111,101,100)
class GrayCode:
    def getGray(self,n):
        if n == 1:
            return ['0','1']
        v = self.getGray(n-1)
        v2 = []
        for i in range(len(v)):
            v2.append('0'+v[i])
        for j in range(len(v)):
            v2.append('1'+v[len(v)-1-j])
        return v2