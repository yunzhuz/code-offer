class solution:
    def find(self,numbers):
        if len(numbers)<=1:
            return False
        if len(numbers)==2:
            if numbers[0]==numbers[1]:
                print('repeat number is:',numbers[0])
            else:
                return False
        
        start=1
        end=len(numbers)-1
        if start<=end:
            middle=(end-start)//2+1
            count=self.counting(numbers,len(numbers),start,middle)
            if count>middle-start+1:
                end=middle
            else:
                start=middle+1

        