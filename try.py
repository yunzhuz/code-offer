while True:
    try:
        pathlist = [] 
        string = input().split(' ')
        a=[]
        path = string[0].split('\\')[-1]
        a.append(path)
        number = string[1]
        a.append(number)
        txt = ' '.join(a)
        wrong = []
        wrong.append(txt)
        new = set(wrong)
        while len(pathlist) <=8:
            for i in range(len(new)):
                b= []
                b.append(new[i])
                for j in range(len(wrong)):
                    count = 1
                    if new[i] == wrng[j]:
                        count+=1
                b.append(count)
            pathlist.append(b)
        print(pathlist)
    except:
        break


while True:
    try:
        dct = dict()
        l = []
        key = input().split('\\')[-1].strip('\n')
        if key not in l:
            l.append(key)
        if key in dct:
            dct[key] = dct[key]+1
        else:
            dct[key] = 1
        result=sorted(dct.item(),key = lambda x:x[1],reverse = True)
        count = 1
        for i in result:
            if count>8:
                break
            count+=1
            if len(i[0].split(' ')[0])>16:
                 print(i[0].split(' ')[0][-16:],i[0].split(' ')[1],i[1])
            else:
                 print(i[0].split(' ')[0],i[0].split(' ')[1],i[1])
    except:
        break
