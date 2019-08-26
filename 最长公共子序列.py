#字符串元素相同时对应的列表在左上角的基础上加1，否则等于左边和上边的数字中较大的一个
string = input()
record = [[0 for i in range(len(string)+1)] for j in range(len(string)+1)] #多创造一行一列，方便字符串中元素相同的时候列表在左上角基础上加一
length = 0
l = []
for i in range(1,len(string)+1):
    index = 1
    for j in range(len(string),0,-1):
        if string[i-1] == string[j-1]:
            record[i][index] = record[i-1][index-1] + 1
            if record[i][index] > length:
                length = record[i][index]
                l.append(string[i-1])
        else:
            record[i][index] = max(record[i][index-1],record[i-1][index])
        index += 1 
print('length is:',length)
print('number of delet:',len(string)-length)
# print(l)
# x=''.join(l)    
# print(x)