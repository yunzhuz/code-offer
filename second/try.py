l = [1,2,3,1,2,3,4,5]
d= {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
d = d.items()
print(d)
# for i in d:
#     if i[1] > 1:
#         print(i[0])