def solution(n):
    a = ''
    for i in range(n):
        a = a + '9'
    maxvalue = int(a)
    for i in range (1,maxvalue+1):
        print(i)

solution(100)