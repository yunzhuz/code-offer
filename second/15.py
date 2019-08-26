def solution(n):
    count = 0
    while n != 0:
        if n&1 == 1:
            count += 1
        n = n >> 1
    return count

def solution(n):
    a = 1
    count = 0
    while a <= n:
        if a & n != 0:
            count += 1
        a = a<<1
    return count

print(solution(9))