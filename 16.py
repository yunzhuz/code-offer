def doublepower(base,exponent):
    if base == 0:
        return 0
    else:
        result = 1
        if exponent == 0:
            return 1
        else:
            for i in range(abs(exponent)):
                result *= base
            if exponent > 0:
                return result
            else:
                return 1/result

##方法2采用递归，加快效率
def doublepower2(base,exponent):
    if base == 0:
        return 0
    result = doublepower2_solution(base,abs(exponent))
    if exponent < 0:
        return 1/result
    else:
        return result
def doublepower2_solution(base,exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = doublepower2(base,exponent >> 1)
    result *= result
    if exponent % 2 == 1:
        result *= base
    return result
        


if __name__ == '__main__':
    print(doublepower(2,-5))
    print(doublepower2(2,-5))
