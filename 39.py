def solution(l):
    l.sort()
    n = len(l)
    dic = {}
    for i in range(n):
        if l[i] in dic:
            dic[l[i]] += 1
        else:
            dic[l[i]] = 1
    dic = dic.items()
    for i in dic:
        if i[1] > (n/2):
            return i[0]

def solution2(l):
    l.sort()
    nl = set(l)
    n = len(l)
    for i in nl:
        count = l.count(i)
        if count > (n/2):
            return i

l = [1,2,3,2,2,2,5,4,2]
print(solution2(l))