def function(array):  #直接逐元素判断奇偶，分别加入两个数组，最后合并
    a1 = []
    a2 = []
    for i in array:
        if i % 2 == 1:
            a1.append(i)
        else:
            a2.append(i)
    for j in a2:
        a1.append(j)
    print(a1)

def function2(array):  #头尾两个指针判断奇偶，若前面为偶后面为奇两者元素互换，否则指针后移或者前移，直到前后指针相遇，思路与快排类似
    left = 0
    right = len(array) -1
    while left < right:
        while left < right and array[left] % 2 == 1:
            left += 1                                                                                                                                                                                                                                         
        while left < right and array[right] % 2 == 0:
            right -= 1
        array[left],array[right] = array[right],array[left]
    print(array)

array = [2,4,3,1,6,5,8]
function(array)
function2(array)