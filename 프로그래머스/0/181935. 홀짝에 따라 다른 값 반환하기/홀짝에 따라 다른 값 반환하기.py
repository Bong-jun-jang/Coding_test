def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n%2 == 1:
            if i%2 == 1:
                answer += i
        elif n%2 == 0:
            if i%2 == 0:
                answer += pow(i,2)
    
    return answer