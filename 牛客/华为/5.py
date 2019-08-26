string = input().strip()
count = [0]*3
n = len(string)
index = 0
while index < n-1:
    if (string[index] > 'a' and string[index] < 'z') or (string[index] > 'A' and string[index] < 'Z'):
        while (string[index+1] > 'a' and string[index+1] < 'z') or (string[index+1] > 'A' and string[index+1] < 'Z'):
            index += 1
        count[0] += 1
        index += 1
    elif string[index] > '0' and string[index] < '9':
        while string[index+1] > '0' and string[index+1] < '9':
            index += 1
        count[1] += 1
        index += 1
    else :
        a = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','"','|','\\',',','<','.','>','/','?']
        while string[index+1] in a:
            index += 1
        count[2] += 1
        index += 1
print(count)
