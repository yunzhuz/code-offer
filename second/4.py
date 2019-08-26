def solution(n,l):
    row = len(l)
    # col = len(l[0])
    for j in range(row):
        for i in l[j]:
            if i == n:
                return True
            else:
                continue
    return False

l= [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(solution(0,l))