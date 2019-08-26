##根据字符串内每个字符出现的次数，按照ASCII码升序调整字符串输出  如输入为eeefgghhh,输出为efghegheh  
string = input().strip()                                      ##  e  3次  先按升序把所有元素输出一边，然后count-1，再循环输出
l = sorted(string)                                            ##  f  1
dic = {}                                                      ##  g  2
for i in l:                                                   ##  h  3
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
dic = dic.items()
count = []
for ele in dic:
    count.append(ele[1])
maxval = count[0]
for i in count:
    if maxval < i:
        maxval = i
n = len(dic)
b = []
for i in l:
    if i not in b:
        b.append(i)
a = []
for j in range(maxval):
    for i in range(n):
        if count[i] > 0:
            a.append(b[i])
        count[i] -= 1       
print(a)