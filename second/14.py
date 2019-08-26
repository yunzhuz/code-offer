def solution(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    f = [0] *(n+1)
    f[1] = 1
    f[2] = 2
    f[3] = 3
    for i in range(4,n+1):
        max = 0
        for j in range(1,int(i/2)+1):
            a = f[j]*f[i-j]
            if a > max:
                max = a
        f[i] = max
    return max
    