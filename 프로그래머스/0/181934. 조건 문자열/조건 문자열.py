def solution(ineq, eq, n, m):
    answer = 0
    if eq is "!":
        if (ineq is ">" and n > m) or (ineq is "<" and n < m):
            answer = 1
        else:
            answer = 0
    else:
        if (ineq is ">" and n >= m) or (ineq is "<" and n <= m):
            answer = 1
        else:
            answer = 0        
    
    return answer