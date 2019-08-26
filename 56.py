def solution(l):
    for i in l:
        if l.count(i) == 1:
            print(i)

def solution1(l):           ##书中提到的方法
    v = 0
    for i in l:     ##所有元素一起异或求和，最终的结果为两个不相同的数字的异或
        v = v^i
    indexoffirst1 = 0
    while v & 1 == 0:          ##找到两个不同数字的异或值的二进制中第一个是1的位置
        indexoffirst1 += 1
        v = v >> 1
    n1 , n2 = 0 , 0
    for j in l:
        if (j >> indexoffirst1) & 1 == 1:
            n1 = n1 ^ j
        else:
            n2 = n2 ^ j
    print(n1,n2)

def solution2(l):  ##利用哈希表即利用字典
    dic = {}
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = dic.items()
    for ele in dic:
        if ele[1] == 1:
            print(ele[0])

l = [2,4,3,6,3,2,5,5]
solution2(l)