x=int(input('please input a number'))
a=[[1,2,3,4,5,6],[7,8,9,10,11,12]]
class solution():
    def find(self,target,array):
        m=len(array)
        n=len(array[0])
        for i in range(m):
            for j in range(n):
                if array[i][j]==target:
                    print('the same number is:',x)


solution().find(x,a)