def solution(l,s):
    row = len(l)
    col = len(l[0])
    for i in range(row):
        for j in range(col):
            if l[i][j] == s[0]:
                dic = [(i,j)]
                if haspath(l,s[1:],row,col,i,j,dic):
                    return True
    return False

def haspath(l,s,row,col,i,j,dic):
    if len(s) == 0:
        return True
    if j+1 < col and (i,j+1) not in dic and l[i][j+1] == s[0]:
        dic.append((i,j+1))
        return haspath(l,s[1:],row,col,i,j+1,dic)
    elif j-1 >= 0 and (i,j-1) not in dic and l[i][j-1] == s[0]:
        dic.append((i,j-1))
        return haspath(l,s[1:],row,col,i,j-1,dic)
    elif i+1 < row and (i+1,j) not in dic and l[i+1][j] == s[0]:
        dic.append((i,j-1))
        return haspath(l,s[1:],row,col,i+1,j,dic) 
    elif i-1 >= 0 and (i-1,j) not in dic and l[i-1][j] == s[0]:
        dic.append((i,j-1))
        return haspath(l,s[1:],row,col,i-1,j)
    else:
        return False

if __name__ =='__main__':
    a=[list('abtg'),
       list('cfcs'),
       list('jdeh')]
    s='bfce'
    b = 'abfb'
    print(solution(a,b))