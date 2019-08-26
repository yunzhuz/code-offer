def solution(l):
    result = []
    for i in range(len(l)):
        if i == l[i]:
            result.append(l[i])
    return result

def solution1(l):  ##只能找到第一个
    result = []
    start, end = 0, len(l) - 1
    while start <= end:
        mid = (start + end) >> 1
        if mid == l[mid]:
            result.append(l[mid])
        elif mid < l[mid]:
            end = mid - 1
        else:
            start = mid + 1

l = [-3,-1,1,3,4,5,7,8]
print(solution(l))