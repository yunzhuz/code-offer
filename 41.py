def solution(l):
    l.sort()
    n = len(l)
    if n % 2 != 0:
        index = n//2
        print(l[index])
    else:
        a = n//2
        b = a - 1
        value = (l[a] + l[b])/2
        print(value)

l = [2,1,3,4,7,5,6,8]
solution(l)