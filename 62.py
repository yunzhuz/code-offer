def solution(n,m):
    l = [i for i in range(n)]
    count = 1
    while len(l) != 1:
        temp = []
        for i in range(len(l)):
            if count % m != 0:
                temp.append(l[i])
            count += 1
        l = temp
        print(l)
    print(l[0])

# def solution1(l):    ##没三个数
#     remove_index = 0
#     zero_number = 0
#     i = 0
#     while True:
#         if zero_number == 4:
#             break
#         if i > 4:
#             i = 0
#         if l[i] != 0:
#             remove_index += 1
#         if remove_index == 3:
#             l[i] = 0
#             remove_index =0
#             zero_number += 1
#         i += 1
#     print(l)

# l = [1,2,3,4,5]
# solution1(l)

class listnode():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def solution1(n,m):
    l = [i for i in range(n)]
    head = listnode(l[0])
    p = head
    for i in l[1:]:
        node = listnode(i)
        p.next = node
        p = p.next
    p.next = head
    np = head
    while n > 1:
        for i in range(m-1):
            np = np.next
        np.data , np.next = np.next.data , np.next.next
        n -= 1
    print(np.data)

solution(5,3)
