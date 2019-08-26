class solution :
    def find(self,numbers):
        if len(numbers)<=1:
            return False
        
        numbers.sort()
        print(numbers)
        repeatarray=[]
        n=0
        for i in range(len(numbers)-1):
            if numbers[i]==numbers[i+1]:
                repeatarray.append(numbers[i])
                print(repeatarray[n])
                n+=1
                
solution().find([2,1,5,2,6,2,1,3,7,0])