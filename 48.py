def solution(s):
    maxlength = 0
    temp = []
    result = []
    for i in range(len(s)):
        currentlength = 0
        l = []
        while i < len(s) and s[i] not in l:
            l.append(s[i])
            currentlength += 1
            i += 1
        if currentlength >= maxlength:
            maxlength = currentlength
            st = ''.join(l)
            temp.append(st)
    for i in temp:
        if len(i) == maxlength:
            result.append(i)
    print(maxlength)
    print(result)

s = 'arabcacfr'
a = 'arabaacfr'
b = 'asdfgh'
d = 'abcabcbb'
solution(d)