import sys

s = []
for line in sys.stdin:
    s.append(sys.stdin.readline().strip())
s=sorted(s)
l = []
for x in s:
    while len(x) >8:
        l.append(x[:8])
        x = x[8:]
    if len(x) <= 8:
        x = x + '0'*(8-len(x))
        l.append(x)
# print(l)
x = ' '.join(l)
print(x)