def calcultion1(n):    #传统递归方法，当n过大时重复计算过多
    if n==0:
        return 0

    elif n==1:
        return 1

    else:
        return calcultion1(n-1)+calcultion1(n-2)

def calcultion2(n):   #循环的方法解决
    if n==0:
        return 0
    
    elif n==1:
        return 1

    else:
        a=0
        b=1
        c=0
        for i in range (2,n+1):
            c=a+b
            a=b
            b=c
        return c

if __name__ == '__main__':
    p=calcultion1(10)
    print(p)
    print(calcultion2(10))