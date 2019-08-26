# #去除重复字符
# string = input().strip()
# l = []
# for i in string:
#     if i not in l:
#         l.append(i)
# x = ''.join(l)
# print(x)


##只去除连续的重复字符
string = input().strip()
n = len(string)
index = 0
l = []
while index < n-1:
    count = 1
    if string[index] == string[index+1]:
        while string[index] == string[index+1]:
            index += 1
            count+=1
        l.append(count)
        l.append(string[index])
        index += 1
    else:
        l.append(string[index])
        index += 1
if string[n-1] != string[n-2]:
    l.append(string[n-1])
result = []
for i in l:
    result.append(str(i))
x = ''.join(result)
print(x)
    