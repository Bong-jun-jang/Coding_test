def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(number in ['0', '5'] for number in str(i)):
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    
    return answer