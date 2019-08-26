def solution(s1,s2):
    if len(s1) != len(s2):
        return False
    l = []
    j = 0
    for i in s1:
        l.append(i)
        while j < len(s1) and l[-1] == s2[j]:
            l.pop()
            j += 1
    if len(l) == 0:
        return True
    else:
        return False


s1 = [1,2,3,4,5]
s2 = [4,5,3,2,1]
print(solution(s1,s2))