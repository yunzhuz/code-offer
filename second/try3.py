s = 'x+2*x=3*x'
try:
    eq = s.replace('=','-(') + ')'
    c = eval(eq,{'x':1j})
    result = -c.real / c.imag
    if result == int(result):
        print(int(result))
    # print(result)
except:
    print(-1)