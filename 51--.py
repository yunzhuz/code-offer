def solution(l):   ##暴力法，每个元素与后面的相比较
    n = len(l)
    count = 0
    for i in range(n-1):
        j = i + 1
        while j < n: 
            if l[i] > l[j]:
                count += 1
            j += 1
    return count

def solution1(data):   ##新建一个排好序的数组，从小到大遍历排好序的数组，找到该数在原数组的位置，count即加上该位置值，然后删除原数组中该元素
    if len(data) <= 0:   ##因为这样每次遍历的元素对于原数组来说都是最小的，那么它在原数组中的index值即表示了原数组中有多少个大于它且位于它前面的数字
        return 0          ### remove每次都是先删除第一次出现的元素，index()方法也是每次先找第一个出现的数字
    count = 0
    copy = []
    for i in range(len(data)):
        copy.append(data[i])
    copy.sort()
    i = 0
    while len(copy) > i:
        count += data.index(copy[i])
        data.remove(copy[i])
        i += 1
    return count


l = [7,6,5,6,4]
s = [8,9,6,7,3,2]
print(solution1(l))
