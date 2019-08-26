def findy(i,j,l,count):
    index = i
    temp = l[i][j]
    count = 0
    while index > 0:
        if temp == l[index-1][j]:
            index -= 1
            count += 1
        else:
            break
    index = i
    while index < 5:
        if temp == l[i+1][j]:
            index += 1
            count += 1
        else:
            break
    return count

def findx(i,j,l,count):
    index = j
    temp = l[i][j]
    while index > 0:
        if temp == l[i][index-1]:
            index -= 1
            count += 1
        else:
            break
    index = j
    while index < 5:
        if temp == l[i][index+1]:
            index += 1
            count += 1
        else:
            break
    return count

def delete(i,j,l):
    indexx = j
    indexy = i
    temp = l[i][j]
    l[i][j] = 'x'
    while indexx > 0:
        if temp == l[i][indexx-1]:
            l[i][indexx-1] = 'x'
            indexx -= 1
        else:
            break
    indexx = j
    while indexx < 5:
        if temp == l[i][indexx+1]:
            l[i][indexx+1] = 'x'
            indexx += 1
        else:
            break
    while indexy > 0:
        if temp == l[indexy-1][j]:
            l[indexy-1][j] = 'x'
            indexy -= 1
        else:
            break
    indexy = i
    while indexy < 5:
        if temm == l[indexy+1][j]:
            l[indexy+1][j] = 'x'
            indexy += 1
        else:
            break

def solution(l):
    for i in range(5):
        for j in range(5):
            while l[i][j] != 'x':
                count = 0
                count = findx(i,j,l,count)
                count = findy(i,j,l,count)
                if count >=3:
                    delete(i,j,l)
                    
        

l = 
i , j = 0,0
solution(i,j,l)