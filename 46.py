def solution(n):
    if n < 0:
        return 0
    s = str(n)
    counts = [None] * len(s)
    for i in range(len(s)-1,-1,-1):
        count = 0
        if i == len(s)-1:
            count = 1
        else:
            count += counts[i+1]
        if i < len(s)-1:
            a = int(s[i]+s[i+1])
            if a >= 10 and a <= 25:
                if i < len(s) - 2:      ##
                    count += counts[i+2]
                else:
                    count += 1
        counts[i] = count
    print(counts[0])

n=112258
solution(n)

            
