class solution():
    def findmin(self,array):
        n=len(array)
        x=array[0]
        for i in range (1,n):
            if array[i]<x:
                x=array[i]
        return x

a=[4,6,1,7,9,3,8]
print(solution().findmin(a))