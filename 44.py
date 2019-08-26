def solution(n):
    l = []
    for i in range(n+1):
        l.append(str(i))
    s = ''.join(l)
    print(s[n])

##方法2 书中提到的解法
def solution1(index):
    i = 1
    while True:
        numbers = countnumber(i)
        if index < numbers * i:
            return getvalue(index,i)
        index -= i*numbers
        i += 1

def countnumber(i):
    if i == 1:
        return 10
    count = pow(10,i-1)
    return count*9

def getvalue(index,i):
    location = index//i
    j = index % i
    if i == 1:
        number = str(location)
    else:
        number = str(pow(10,i-1) + location)
    return number[j]


solution(1001)
print(solution1(1001))