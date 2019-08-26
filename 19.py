def solution(string,p):
    if len(string) == 0 and len(p) == 0:
        return True
    if len(string) > 0 and len(p) == 0:
        return False
    if len(p) > 1 and p[1] == '*':
        ##如果模式的第二个字符为*时有三种情况
        if len(string) > 0 and (string[0] == p[0] or p[0]=='.'):
            ## 1、模式后移2个字符，此时*表示0次  如aaa 和a*aaa匹配时，忽略a*可以匹配成功
            ## 2、字符串后移一个，模式后移两个，此时*表示1次
            ## 3、字符串后移一个，模式不变，继续匹配字符串中下一个，此时*表示多次
            return solution(string,p[2:]) or solution(string[1:],p[2:]) or solution(string[1:],p)
        else:
            return solution(string,p[2:])
    if len(string) > 0 and (string[0] == p[0] or p[0] == '.'):
        return solution(string[1:],p[1:])
    else:
        return False

string = 'aaa'
p = 'a.*'
print(solution(string,p))
