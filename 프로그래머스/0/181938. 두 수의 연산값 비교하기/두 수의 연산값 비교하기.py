def solution(a, b):
    answer = 0
    
    st = str(a)+str(b)
    dou = 2 * a * b
    
    if int(st) >= dou:
        answer = int(st)
    else:
        answer = dou
    
    return answer