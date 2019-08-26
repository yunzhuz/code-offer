def quicksort(array,left,right):
        if right > left:
            k = function(array,left,right)
            quicksort(array,left,k)
            quicksort(array,k+1,right)
        else:
            return
        

def function(array,left,right):
    k=array[right]
    i = left -1
    for j in range(left,right):
        if array[j] <= k:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[right] = array[right],array[i]
    return i

arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
quicksort(arr,0,len(arr)-1)
print(arr)