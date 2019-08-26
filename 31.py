def solution(s1,s2):
    if len(s1) != len(s2):
        return False
    stack = []
    j = 0
    for i in s1:
        stack.append(i)
        while stack and stack[-1] == s2[j]:
            stack.pop()
            j += 1
    if len(stack) == 0 :
        return True
    else:
        return False

s1 = [1,2,3,4,5]
s2 = [4,3,5,1,2]
print(solution(s1,s2))