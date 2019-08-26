s = 'acadb'
s = sorted(s)
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1
d = d.items()
print(d)
l = []
for i in d:
    l.append(i[0])
    l.append(str(i[1]))
x = ''.join(l)
print(x)