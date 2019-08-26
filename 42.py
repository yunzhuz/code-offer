def solution(l):
    if not l:
        return 0
    a = 0
    result = 0
    for i in l:
        if a <= 0:
            a = i
        else:
            a += i
        if a > result:
            result = a
    return result

l1 = [1,-2,3,10,-4,7,2,-5]
l=[-10,2,3]
print(solution(l1))