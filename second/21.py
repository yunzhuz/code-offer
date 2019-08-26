def solution(l):
    a = []
    b = []
    for i in l:
        if i % 2 == 1:
            a.append(i)
        else:
            b.append(i)
    c = a+b
    print(c)

def solution2(l):
    left = 0
    right = len(l) - 1
    while left < right:
        while left < right and l[left] % 2 == 1:
            left += 1
        while left < right and l[right] % 2 == 0:
            right -= 1
        l[left] , l[right] = l[right] , l[left]
    print(l)

l = [1,2,3,4,5,6,7,8,9,10,11]
solution2(l)
