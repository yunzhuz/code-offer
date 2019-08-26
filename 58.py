def solution(s):
    l = s.split(' ')
    #l = l[::-1]
    l.reverse()
    result = ' '.join(l)
    print(result)

##题目二
def solution1(s,n):
    l = []
    for i in s:
        l.append(i)
    a = []
    for i in range(n):
        a.append(l[i])
    for j in a:
        l.remove(j)
    return ''.join(l) + ''.join(a)


# s = 'I am a student.'
# solution(s)
a = 'abcdefg'
print(solution1(a,2))