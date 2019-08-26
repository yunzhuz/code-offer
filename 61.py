def solution(l):
    l.sort()
    n = 0
    for i in l:
        if i == 0:
            n += 1
    index = n
    gap = 0
    while index < len(l)-1:
        if l[index] == l[index + 1]:
            return False
        gap += l[index+1] - l[index] - 1
        index += 1
    if gap > n:
        return False
    else:
        return True

l = [2,4,0,0,7]
print(solution(l))