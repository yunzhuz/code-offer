def solution(l,s): ##暴力法
    i = 0
    result = []
    while i < (len(l)-2):
        j = i+1
        while j <(len(l)-1):
            if l[i] + l[j] == s:
                result.append([l[i],l[j]])
            j += 1
        i += 1
    return result

def solution1(l,s):  ##确定两个指针
    left = 0
    right = len(l) - 1
    while left < right:
        if l[left] + l[right] < s:
            left += 1
        elif l[left] + l[right] > s:
            right -= 1
        else:
            return[l[left],l[right]]

##题目二
def solution2(s):
    if s < 3:
        return []
    left , right = 1 , 2
    result = []
    while left < (s/2) :
        count = 0
        for i in range(left,right+1):
            count += i
        if count < s:
            right += 1
        elif count > s:
            left += 1
        else:
            result.append(list(range(left,right+1)))
            right += 1
    return result

# l = [1,2,4,7,8,11,15]
# print(solution(l,15))
print(solution2(15))