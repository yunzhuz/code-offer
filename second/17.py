def solution(n):
    s = ''
    for i in range(n):
        s += '9'
    max = int(s)
    for i in range(1,max):
        print(i)