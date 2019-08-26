def findmin(array):
    if not array:
        return

    if len(array)==2:
        if array[0]<array[1]:
            return array[0]
        else:
            return array[1]

    start = 0
    end = len(array)-1
    mid = start
    while end-start!=1:
        mid = start+(end-start)//2
        # print('mid=',mid)
        if array[mid] >= array[start]:
            start = mid
            # print('start=',start)
        if array[mid] <= array[end]:
            end = mid
            # print('end=',end)

    return array[end]

if __name__ =='__main__':
    a=[3,4,5,6,1,2]
    a1=[5,6,1,2,3,4]
    a2=[1,2,3,4]
    a3=[]
    print(findmin(a2))        
