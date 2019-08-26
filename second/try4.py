from fractions import Fraction
n=2
count = 0
for i in range(1,n+1):
    temp = Fraction(1,i)
    count += temp
print(count)