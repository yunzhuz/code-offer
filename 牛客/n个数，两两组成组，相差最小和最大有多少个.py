while 1:
    try:
        n = int(input())
        array = (input().strip()).split(' ')
        l = []
        for i in array:
                l.append(int(i))
        l.sort()
        minvalue = l[0]
        maxvalue = l[-1]
        if minvalue == maxvalue:
            count = n*(n-1)//2
            print(count,count)
        else:
            maxcount = 0
            mincount = 0
            dic = {}
            for i in range(n):
                if l[i]in dic:
                    dic[l[i]] += 1
                else:
                    dic[l[i]] = 1
            maxcount = dic[l[0]] * dic[l[-1]]
            dic = dic.items()
            if len(dic) != n:
                for key in dic:
                    mincount += key[1] * (key[1]-1) //2
            else:
                a = []
                for i in range(1,n):
                    a.append(l[i]-l[i-1])
                a.sort()
                i = 1
                mincount = 1
                while a[i] == a[0]:
                    mincount +=1
                    i+=1
            print(mincount,maxcount)
    except:
        break
