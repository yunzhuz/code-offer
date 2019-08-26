def solution(l):
    i = 0
    while i < len(l):
        if l[i] == i:
            i += 1
        else:
            index = l[i]
            if l[index] == l[i]:
                return True
            else:
                l[i] , l[index] = l[index] , index
    if i == len(l):
        return False

l = [2,3,1,0,2,5,3]
a = [0,5,4,3,1,2]
print(solution(a))