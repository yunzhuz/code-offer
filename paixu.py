def maopao(array):    #冒泡总共比较数个数减1趟，每趟循环中比较相邻元素的大小，并判断是否交换位置，将最大元素沉到末尾
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                a = array[j]
                array[j] = array[j+1]
                array[j+1] = a
        print('每次排序后结果：',array)

def xuanze(array):   #选择排序总共比较n-1趟，第i次比较从数组中第（i-1）位开始，假设第一个元素为最小，找出后面是否有最小的元素，有就交换位置
    for i in range(len(array)-1):
        minindex = i
        for j in range(i+1,len(array)):
            if array[minindex] > array[j]:
                minindex = j
        a = array[i]
        array[i] = array[minindex]
        array[minindex] = a
        print('每次排序后结果：',array)

def charu(array):
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            a = array[i]
            index = i
            for j in range(i-1,-1,-1):
                if array[j] > a:
                    array[j+1] = array[j]
                    index = j
                else:
                    break
            array[index] = a
            print('每次排序后结果：',array)

class kuaipai():
    def quicksort(self,l,left,right):
        if left < right:
            k = self.function(l,left,right)
            self.quicksort(l,left,k-1)
            self.quicksort(l,k+1,right)
        return l
    def function(self,l,low,high):
        left , right =  low , high
        temp = l[left]
        while left < right:
            while l[left] <= temp:
                left += 1
            while l[right] > temp:
                right -= 1
            if left < right:
                l[left] , l[right] = l[right] , l[left]
        l[low] = l[right]
        l[right] = temp
        return right
            
# print(kuaipai().quicksort([10,1,35,61,89,36,55],0,6))
maopao([3,1,6,4,5,0])

