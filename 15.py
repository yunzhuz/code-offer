def solution(n):
    count = 0
    while n!= 0:
        if n&1 == 1:
            count+=1
        n = n >> 1
    return count

def solution2(n):
    count = 0
    a=1
    while a <= n:
        if n & a !=0:
            count+=1
        a = a << 1
    return count

def solution3(n):
    count = 0
    while n != 0:
        count += 1
        n = n & (n-1)
    return count
if __name__ == '__main__':
    print(solution(9))
    print(solution2(9))
    print(solution3(9))