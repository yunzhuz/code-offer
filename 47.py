def solution(l):
    if not l:
        return 0
    row , col = len(l) , len(l[0])
    maxvalue = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            left ,up = 0 , 0
            if i > 0:
                up = maxvalue[i-1][j]
            if j > 0:
                left = maxvalue[i][j-1]
            maxvalue[i][j] = max(left,up) + l[i][j]
    print(maxvalue)
    print(maxvalue[row-1][col-1])

def solution1(l):
    if not l:
        return 0
    row , col = len(l) , len(l[0])
    maxvalue = [0 for i in range(col)]
    for i in range(row):
        for j in range(col):
            left , up = 0 , 0
            if i > 0:
                up = maxvalue[j]
            if j > 0:
                left = maxvalue[j-1]
            maxvalue[j] = max(up,left) + l[i][j]
    print(maxvalue)
    print(maxvalue[col-1])

l =[[1,10,3,8],
    [12,2,9,6],
    [5,7,4,11],
    [3,7,16,5]]
solution(l)
solution1(l)