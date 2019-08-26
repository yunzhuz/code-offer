##计算输入加减运算式的值
# l = input().strip().split(' ')
# if len(l) != 3:
#     print("0")
# else:
#     a = int(l[0])
#     b = int(l[2])
#     if l[1] == '+':
#         result = a + b
#         print(result)
#     elif l[1] == '-':
#         result = a - b
#         print(result)
#     else:
#         print('0')

# 计算输入数据中的最大值和最小值的和
l = input().strip().split(',')
a = []
for i in l:
    a.append(int(i))
l = sorted(a)
result = l[0] + l[-1]
print(result)