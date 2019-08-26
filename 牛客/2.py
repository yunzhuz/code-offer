l1 = input().strip().split(' ')
n = int(l1[0])
m = int(l1[1])
l2 = list(map(int,input().strip().split(' ')))
l3 = list(map(int,input().strip().split(' ')))
mi , ma ,i = l2[0] , 0 , 0
# minindex , maxindex = 0 , 0
while i < n:
    if l2[i] < mi:
        mi = l2[i]
        # minindex = i
    if l2[i] > ma:
        ma = l2[i]
        # maxindex = i
    i += 1
maxvalue , p = 0 , 0
for i in range(n):
    maxvalue += l3[i] * (ma-l2[i]) 
    p += l3[i]
if maxvalue > m:
    while maxvalue > m and ma>0:
        ma -= 1
        maxvalue = 0
        for i in range(n):
            maxvalue += l3[i] * max((ma-l2[i]),0)
else:
    while maxvalue < m:
        ma += 1
        maxvalue += p
print(ma)