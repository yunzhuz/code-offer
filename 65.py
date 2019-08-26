def solution(m,n):
    l = [m,n]
    return sum(l)

def solution1(m,n):
    while n != 0:
        sum = m ^ n
        temp = (m & n) << 1
        m = sum
        n = temp
    return sum
 
print(solution(11,2))