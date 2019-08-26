def solution(base , exponent):
    if base == 0:
        return 0
    else:
        if exponent == 0 :
            return 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if exponent > 0:
            return result
        else:
            return 1/result

def solution2(base,exponent):
    if base == 0:
        return 0
     result = solution2_doublepower(base,exponent)
     if exponent < 0:
         return 1/result
    else:
        return result

def solution2_doublepower(base,exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = solution2_doublepower(base,exponent >> 1)
    result *= result
    if exponent % 2 ==1:
        result *= base
    return result

print(solution(2,-3))