def solution(l,n):
    return l.count(n)

def solution1(l,n):    ##二分法找到一个k，然后在左右两边扫描找k
    start , end = 0 , len(l)-1
    while start <= end:
        mid = int((end + start) / 2)
        if l[mid] > n:
            end = mid - 1
        if l[mid] < n:
            start = mid + 1
        if l[mid] == n:
            break
    count = 0
    index = mid
    while l[index] == n:
        count += 1
        index -= 1
    while l[mid+1] == n:
        count += 1
        mid += 1
    return count

def solution2(l,n):    ##二分法找到第一个和最后一个n，然后index相减
    first = getfirst(l,n)
    last = getlast(l,n)
    if first >= 0 and last >= 0:
        count = last - first + 1
    return count

def getfirst(l,n):
    start , end = 0 , len(l)-1
    while start <= end:
        mid = int((end + start) / 2)
        if l[mid] == n:
            if (l[mid-1] != n and mid>0) or mid == 0:
                return mid
            else:
                end = mid -1
        elif l[mid] > n:
            end = mid - 1
        else:
            start = mid + 1

def getlast(l,n):
    start , end = 0 , len(l)-1
    while start <= end:
        mid = int((end + start) / 2)
        if l[mid] == n:
            if (l[mid+1] != n and mid <len(l)-1) or mid ==len(l)-1:
                return mid
            else:
                start = mid + 1
        elif l[mid] > n:
            end = mid -1
        else:
            start = mid + 1

l = [1,2,3,3,3,4,4,5]
s = [1,2,3,4,5,6,7,8]
print(solution2(l,3))
 