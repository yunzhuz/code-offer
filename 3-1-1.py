def find(array):
    l= []
    for i in array:
        if i not in l:
            l.append(i)
    a=[]
    for m in range(len(l)):
        count = 0
        for n in range(len(array)):
            if array[n] == l[m]:
                count += 1
        if count >= 2:
            a.append(l[m])
    for j in range(len(a)):
        print("repeate:",a[j])
find([2,1,5,2,6,2,1,3,7,0,2,3,2,6,9,6])