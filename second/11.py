def solution(l):
    if len(l) == 2:
        print(l[1])
    if l[0] < l[-1]:
        print(l[0])
    else:
        first , last = 0 , len(l)-1
        while first < last-1:
            mid = (last + first)//2
            if l[mid] >= l[first]:
                first = mid
            if l[mid] < l[first]:
                last = mid
        if l[first] < l[last]:
            print(l[first])
        else:
            print(l[last])

l = [3,4,5,6,1,2]
b=[1,2,3,4,5]
a = [5,6,1,2,3,4]
solution(b)
