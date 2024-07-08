def solution(numLog):
    answer = ''
    check = 0
    swich = {
        1:  "w",
        -1: "s",
        10: "d",
        -10: "a",
        0: ""
    }

    for i in range(len(numLog)):
        if i > 0:
            check = numLog[i] - numLog[i-1]
        answer += swich[check]
    
    return answer