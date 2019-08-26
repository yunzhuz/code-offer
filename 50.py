def solution(s):
    l = []
    dic = {}
    for i in s:                ##这样产生的dic里面的元素顺序是随机的，即每次的dic里面元素顺序可能都不同
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1 
    print(dic)
    for j in s:
        if dic[j] == 1:
            l.append(j)
    print(l)
    print(l[0])
    # dic = dic.items()
    # # print(dic)
    # for ele in dic:
    #     if ele[1] == 1:
    #         return ele[0]
    # #         l.append(ele[0])
    # # print(l)
    # # print(l[0])

def solution1(s):
    l = []
    result = []
    for i in s:
        l.append(i)
    for j in l:
        if l.count(j) == 1:
            result.append(j)
    print(result)
    print(result[0])

s = 'abaccdeff'
# solution(s)
#print(solution(s))
solution(s)