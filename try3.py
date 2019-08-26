while True:
    try:
        array=[]
        n=int(input())
        for i in range(n):
            array.append(int(input()))
        result = []
        for a in array:
            if a not in result:
                result.append(a)
        for i in range(1,len(result)):
            if result[i] < result[i-1]:
                a = result[i]
                index = i
                for j in range (i-1,-1,-1):
                    if result[j] > a:
                        result[j+1] = result[j]
                        index = j
                    else:
                        break
                    result[index] = a
        for j in range (len(result)):
            print(result[j])
    except:
        break