import sys
def solution(l,p):
    if len(l) == 0:
        return p
    elif l[0] == l[1]:
        p.append(l[0])
        solution(l[2:],p)
    else:
         False
for line in sys.stdin:
    line =  line.strip()
    if len(line) % 2 != 0:
        print('false')
    elif line != line[::-1]:
        print('false')
    else:
        l = []
        for i in line:
            l.append(i)
        p = []
        solution(l,p)
        x = ''.join(p)
        print(x)
        # x = ''.join(result)
        # print(x)