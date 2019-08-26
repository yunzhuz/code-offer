def solution(l,n):
    result = []
    i = 0
    while i < len(l)-n+1:
        maxvalue = 0
        for j in range(i , i+n):
            if l[j] > maxvalue:
                maxvalue = l[j]
        i += 1
        result.append(maxvalue)
    return result

l = [2,3,4,2,6,2,5,1]
print(solution(l,3))