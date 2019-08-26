def solution(l):
    n = len(l)
    b = [0] * n
    for i in range(n):
        left , right = 1 , 1
        if i ==0:
            temp = 1
            for m in range(1,n):
                temp *= l[m]
            b[i] = temp
        elif i >= 1 and i < n-1:
            j = 0
            while j < i:
                left *= l[j]
                j += 1
            ele = i
            while ele < n-1:
                right *= l[ele+1]
                ele += 1
            b[i] = left * right
        else:
            temp = 1
            for m in range(n-1):
                temp *= l[m]
            b[i] = temp
    print(b)

a = [2,3,4,5,6]
solution(a)  