import sys 
def solution(l,p,st):
    if len(l) == 0:
        return p
    else:
        b = ''
        index = 0
        while b not in st:
            b = b + l[index]
            index += 1
        p.append(st.index(b))
        solution(l[index:],p,st)

for line in sys.stdin:
    a = line.strip()
    n = len(a)
    a.lower()
    st = ['zero','one','two','three','four','five','six','seven','eight','nine']
    l = []
    for i in a:
        l.append(i)
    p = []
    solution(l,p,st)
    x = ''.join(p)
    print(x)