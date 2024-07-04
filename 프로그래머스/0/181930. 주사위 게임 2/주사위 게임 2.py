def solution(a, b, c):
    answer = 0
    if a == b and a == c and b == c:
        answer = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) *\
        (pow(a, 3) + pow(b, 3) + pow(c, 3))
    elif a == b or a == c or b == c:
        answer = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2))
    else:
        answer = a + b + c
        
    return answer