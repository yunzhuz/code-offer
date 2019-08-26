l = input().strip().split(' ')
print(l)
a = []
for i in l:
    if i != '':
        a.append(i)
print(a)
result = a[::-1]
x = ' '.join(result)
print(x)