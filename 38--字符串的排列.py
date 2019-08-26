def solution(s):
    if not s:
        return []
    if len(s) == 1:
        return list(s)
    result = []
    l = list(s)
    l.sort()
    for i in range(len(l)):
        if i > 0 and l[i] == l[i-1]: ##先对字符串进行了排序，然后这里消除重复元素的影响
            continue
        temp = solution(''.join(l[:i]) + ''.join(l[i+1:]))
        for j in temp:
            result.append(l[i]+j)
    return result

s = 'abc'
print(solution(s))