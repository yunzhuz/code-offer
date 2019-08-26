class Gift:
    def getValue(self, gifts, n):
        # write code here
        dic = {}
        gifts.sort()
        for i in range(n):
            if gifts[i] in dic:
                dic[gifts[i]] += 1
            else:
                dic[gifts[i]] = 1
        dic = dic.items()
        for i in dic:
            if i[1] >  (n/2):
                return i[0]
        return 0
while 1:
    try:
        a = (raw_input().strip()).replace('[','').replace(']','').split(',')
        n = int(a[-1])
        gifts = a[:-1]
        print(Gift().getValue(gifts,n))
    except:
        break