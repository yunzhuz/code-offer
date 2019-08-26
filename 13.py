def move(threshold,row,col):
    if threshold <0 or row <0 or col <0:
        return False
    array=[[0 for i in range(row)]for j in range(col)]
    count = movecounting(threshold,row,col,0,0,array)
    return count

def movecounting(threshold,row,col,i,j,array):
    count = 0
    if check(threshold,row,col,i,j,array):
        array[i][j] = True    #必须判断是否已经经过该格子，如果下面判断句中没有not array[i][j]，将陷入死循环中，一直在i=0,j=0和i=1，j=0两个格子之间循环
        count = 1+ movecounting(threshold,row,col,i-1,j,array) \
                 + movecounting(threshold,row,col,i+1,j,array) \
                 + movecounting(threshold,row,col,i,j-1,array) \
                 + movecounting(threshold,row,col,i,j+1,array)
    return count

def check(threshold,row,col,i,j,array):
    if 0 <= i < row and 0 <= j < col and not array[i][j]:   ##最后一个判断式子判断是否已经经过该格子，经过的格子已赋值true，not true为不满足条件,这就和12题中要判断当前格子字符是否等于新字符串的第一个字符一样
        a=0
        for index in str(i):
            a+=int(index)
        for index in str(j):
            a+=int(index)
        if a <= threshold:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    print(move(3,5,5))