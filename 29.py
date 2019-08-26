def solution(a):
    row = len(a)
    col = len(a[0])
    count = 0    ##count表示每次循环打印数字时的起始行列数
    while row > count*2 and col > count*2:
        printvalue(a,row,col,count)
        count += 1

def printvalue(a,row,col,count):
    maxx = col - 1 - count
    maxy = row - 1 - count
    for i in range(count , maxx+1):   ##从左向右打印一行
        print(a[count][i] , end=' ')
    if maxy > count:        ##从上到下打印一列，必须满足最大行数大于起始行数
        for i in range(count+1,maxy+1):
            print(a[i][maxx] , end=' ')
    if maxy > count and maxx > count:   ##从左到右打印一行，需满足最大行数大于起始行数，最大列数大于起始列数
        for i in range(maxx-1 , count-1 , -1):
            print(a[maxy][i] , end=' ')
    if maxx > count and maxy - 1 > count:    ##从 上到下打印一列，需满足最大列数大于其实列数，同时最大行数比起始行数大2（从左到右打印时已经打印第一个数）
        for i in range(maxy-1,count,-1):
            print(a[i][count] , end=' ')

if __name__ == "__main__":
    a = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
    solution(a)