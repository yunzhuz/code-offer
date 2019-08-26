def solution(n):
    if n < 0:
        return
    number , count = 0,0
    while count != n:
        number += 1
        if isugly(number):
            count += 1
    return number
        
def isugly(i):
    while i % 2 == 0:
        i = i/2
    while i % 3 == 0:
        i = i/3
    while i % 5 == 0:
        i = i/5
    if i == 1:
        return True
    else:
        return False

def solution1(index):
    if index <= 0:
        return 0
    l = [1]
    a2 , a3 , a5 = 0 , 0 , 0
    while len(l) < index:
        minvalue = min(l[a2]*2 , l[a3]*3 , l[a5]*5)
        l.append(minvalue)
        while l[a2]*2 <= l[-1]:
            a2 += 1
        while l[a3]*3 <= l[-1]:
            a3 += 1
        while l[a5]*5 <= l[-1]:
            a5 += 1
    return l[-1]
    

#print(solution(105))
print(solution1(150))