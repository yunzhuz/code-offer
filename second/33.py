def solution(s):
    if len(s) == 1 or len(s) == 0:
        return True
    midvalue = s[-1]
    left = []
    right = []
    i = 0
    while s[i] < midvalue:
        left.append(s[i])
        i += 1
    right = s[i:-1]
    for i in right:
        if i < midvalue:
            return False
    return solution(left) and solution(right)

if __name__ == '__main__':
    s = [5,7,6,9,11,10,8]
    s2 = [7,4,6,5]
    s3 = [6,5,4,8,9,10,7]
    s4 = [4,6,7,5]
    print(solution(s4))