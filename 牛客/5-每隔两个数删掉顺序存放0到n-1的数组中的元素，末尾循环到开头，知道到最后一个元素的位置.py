while 1:
    try:
        n = int(input())
        array = [i for i in range(n)]
        count = 1
        while len(array) != 1:
            temp = []
            for i in range(len(array)):
                if count %3 != 0:
                    temp.append(array[i])
                count += 1
            array = temp
        print(array[0])
    except:
        break