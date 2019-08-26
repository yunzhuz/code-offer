def maxproduct(n):
    if n < 2:
        return False
    if n==2:
        return 1
    if n==3:
        return 2
    f=[0]*(n+1)
    f[1] = 1
    f[2] = 2
    f[3] = 3
    for i in range(4,n+1):
        max=0
        for j in range(1,int(i/2)+1):
            a=f[j] * f[i-j]
            if a > max:
                max = a
        f[i] = max
    return f[n]

def maxproduct2(n):   #贪婪算法 尽可能多的剪出长度为3的绳子，当剩下的长度为1时，要少剪一个3，变成4，剪为两个2
    if n<2:
        return False
    if n == 2:
        return 1
    if n == 3:
        return 2
    a = n//3
    if n - a*3 ==1:
        a-=1
    b = (n- a*3)/2
    return int(pow(3,a)*pow(2,b))

if __name__ == '__main__':
    print(maxproduct(10))
    print(maxproduct2(10))