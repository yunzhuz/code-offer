l = input().strip().split(' ')
for i in range(len(l)):
    l[i] = int(l[i])
nl = []
for i in l:
    if i not in nl:
        nl.append(i)
    else:
        print(i)