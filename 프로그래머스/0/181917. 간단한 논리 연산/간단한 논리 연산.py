def solution(x1, x2, x3, x4):
    answer = True
    val1 = x1 or x2
    val2 = x3 or x4
    answer = val1 and val2
    
    return answer