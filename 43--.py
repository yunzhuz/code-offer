def solution(n):
    if n <= 0:
        return 0
    count = 0
    for i in range(1,n+1):
        while i != 0:
            if i % 10 == 1:
                count += 1
            i = i // 10
    return count

print(solution(11658))