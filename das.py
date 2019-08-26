def solution(l):
    count = 1
    while len(l) != 1:
        temp = []
        for i in range(len(l)):
            if count % 3 != 0:
                temp.append(l[i])
            count += 1
        l = temp
    print(l[0])

def solution1(l):
    remove_index = 0
    zero_number = 0
    i = 0
    while True:
        if zero_number == 4:
            break
        if i > 4:
            i = 0
        if l[i] != 0:
            remove_index += 1
        if remove_index == 3:
            l[i] = 0
            remove_index =0
            zero_number += 1
        i += 1
    print(l)

l = [1,2,3,4,5]
solution1(l)