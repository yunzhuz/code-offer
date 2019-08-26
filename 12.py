def haspath(lis,s):
    if not lis or not s:
        return
    
    row=len(lis)
    col=len(lis[0])
    for i in range(row):    #这里i和j的取值在0到行数和列数之间
        for j in range(col):
            dic = []
            if findpath(lis,s,row,col,i,j,dic):
                return True
    return False

def findpath(lis,s,row,col,i,j,dic):
    if not s:
        return True
    # panduan = False
    if i>=0 and j>=0 and i<row and j<col  and (i,j) not in dic and lis[i][j]== s[0]:    #注意i和j是<行数和列数，不能是<=，i和j为下标必须小于行数和列数否则列表超出
        dic.append((i,j))
        panduan = findpath(lis,s[1:],row,col,i,j-1,dic) or \
                   findpath(lis,s[1:],row,col,i,j+1,dic) or \
                   findpath(lis,s[1:],row,col,i-1,j,dic) or \
                   findpath(lis,s[1:],row,col,i+1,j,dic)
        return panduan
    else:
        return False

if __name__ =='__main__':
    a=[list('abtg'),
       list('bbbb'),
       list('cfcs'),
       list('jdeh')]
    s='bbfce'
    c = 'abbfb'
    print(haspath(a,s))