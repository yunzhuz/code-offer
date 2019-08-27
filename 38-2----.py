def solution(s):
    l = list(s)
    result = []
    for i in range(1,len(l)+1):
        zuhe(l,result,i)

def zuhe(l,result,m):
    if len(result) == m:
        print(''.join(result))
        return
    if l:
        result.append(l[0])
        zuhe(l[1:],result,m)
        result.pop()
        zuhe(l[1:],result,m)
        
s = 'abc'
solution(s)
        
