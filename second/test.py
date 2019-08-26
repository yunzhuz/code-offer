def solution(string,p):
    if len(string) == 0 and len(p) == 0:
        return True
    if len(string) > 0 and len(p) == 0:
        return False
    if len(p) > 1 and p[1] == '*':
        if len(string) > 0 and (string[0] == p[0] or p[0] == '.'):
            return solution(string[1:],p[2:]) or solution(string[1:],p) or solution(string,p[2:])
        else:
            return solution(string,p[2:])
    if len(string) > 0 and (string[0] == p[0] or p[0] == '.'):
        return solution(string[1:],p[1:])
    else:
        return False
    
string = 'aaa'
p = 'a.a'
print(solution(string,p))