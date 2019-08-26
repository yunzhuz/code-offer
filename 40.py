def solution(l,k):
    l.sort()
    for i in range(k):
        print(l[i])

l = input().split(',')
#print(l)
solution(l,4)