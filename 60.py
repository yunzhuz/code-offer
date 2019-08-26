class f1():   ##方法1.先固定一个骰子，遍历每个值并分别和其他骰子的值相加，将出现的和以及次数加入字典中
    def solution(self,n):
        if n < 1:
            return
        total = pow(6,n)
        dct = {}
        for i in range(1,7):
            self.probability(i,n,dct)
        for ele in dct.items():
            print('%d %.6f'%(ele[0],ele[1]/total))

    def probability(self,i,n,dct):
        if n == 1:
            dct[i] = dct.get(i,0) + 1   ##dict.get(a,b) 返回字典中键值为a的值，若没有a返回b，若不指定b找不到时则返回none
        else:
            for j in range(1,7):
                self.probability(j+i,n-1,dct)

def solution2(n): 
    total = pow(6,n)
    l =[[0]*(6*n+1) , [0]*(6*n+1)]
    flag = 0
    for i in range(1,7):
        l[flag][i] = 1
    for j in range(2,n+1):
        for k in range(j,6*j+1):
            l[1-flag][k] = 0    ##一定要重新赋0值，否则下面累积相加的时候会把上次循环时叠加的值加进去
            a = 1
            while a <= k and a <=6:
                l[1-flag][k] += l[flag][k-a]
                a += 1
        flag = 1-flag
    for i in range(n,6*n+1):
        ratio = l[flag][i]/total
        print('%d %.6f'%(i,ratio))


f1().solution(3)
print('------')
solution2(3)