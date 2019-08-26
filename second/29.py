def solution(l):
    row = len(l)
    col = len(l[0])
    index = 0
    while row > index * 2 and col > index*2:
        printvalue(l,index,row,col)
        index += 1

def printvalue(l,index,row,col):
    maxx = col - index - 1
    maxy = row - index - 1
    for i in range(index,maxx+1):
        print(l[index][i] , end=' ')
    if maxy > index:
        for i in range(index+1,maxy+1):
            print(l[i][maxx],end=' ')
    if maxy > index and maxx > index:
        for i in range(maxx-1,index-1,-1):
            print(l[maxy][i],end=' ')
    if maxx > index and maxy-1 > index:
        for i in range(maxy-1,index,-1):
            print(l[i][index],end=' ')

if __name__ == "__main__":
    a = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
    solution(a)