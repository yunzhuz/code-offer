def solution(l,s,count):
    a = s%l[0]
    b = s//l[0]
    count += b
    while s != 0:
        if a == 0:
            return(count)
        else:
            res = s - b*l[0]
            solution(l[1:],res,count)
    return -1
n = int(input().strip())
l = list(map(int,input().strip().split(' ')))
s = int(input().strip())
l = sorted(l,reverse=True)
count = 0
result = solution(l,s,count)
print(result)