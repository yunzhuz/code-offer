while 1:
    try:
        n = input().split('-')
        n1 = n[0].split(' ')
        n2 = n[1].split(' ')
        string = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
        if 'joker JOKER' in n:
            print('joker JOKER')
        else:
            if len(n1) == len(n2):
                if string.index(n1[0]) > string.index(n2[0]):
                    print(n[0])
                else:
                    print(n[1])
            elif len(n1) ==4 and len(n2)!= 4:
                print(n[0])
            elif len(n2) == 4 and len(n1)!=4:
                print(n[1])
            else:
                print('ERROR')
    except:
        break