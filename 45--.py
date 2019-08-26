from functools import cmp_to_key

def solution(l):
    if not l:
        return
    cm = cmp_to_key(lambda x,y:int(str(x)+str(y))-int(str(y)+str(x)))
    result = sorted(l,key=cm)
    print(result)
    return ''.join(str(i) for i in result)

def solution1(l):
    if not l:
        return
    result = []
    

l = [3,32,321]
s = [3,55,11,4,2]
print(solution(s))