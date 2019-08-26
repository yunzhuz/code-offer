def solution(l):
    for i in range(len(l)):
        if i != l[i]:
            return i

def solution1(l):
    start , end = 0 , len(l)-1
    while start <= end:
        mid = int((start + end)/2)
        if l[mid] == mid:
            start = mid + 1
        else:
            if (mid > 0 and l[mid-1] == mid -1) or mid == 0:
                return mid
            else:
                end = mid -1

l = [0,1,2,4,5,6]
s = [1]
print(solution1(s))