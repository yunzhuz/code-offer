l = input().strip().split(' ')
n = int(l[0])
k = int(l[1])
h = list(map(int,input().strip().split(' ')))
i = 0
min = 0
index = 0
for b in range(k):
    min += h[b]
while i <= n-k:
    temp = 0
    for j in range(i,i+k):
        temp += h[j]
    if temp < min:
        min = temp
        index = i
    i += 1
print(index+1)