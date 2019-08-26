def solution(l):
    maxvalue = 0
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            temp = l[j] - l[i]
            if temp > maxvalue:
                maxvalue = temp
    print(maxvalue)

def solution1(l):
    minvalue = l[0]
    maxdiff = l[1] - minvalue
    for i in range(2,len(l)):
        if l[i-1] < minvalue:
            minvalue = l[i-1]
        temp = l[i] - minvalue
        if temp > maxdiff:
            maxdiff = temp
    print(maxdiff)

l = [9,11,8,5,7,12,16,14]
solution1(l)
