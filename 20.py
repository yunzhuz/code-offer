def function(st):
    try:
        result = float(st)
        print(result)
    except:
        print('false')

st = '12e'
function(st)
