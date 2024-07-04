def solution(num_list):
    answer = 0
    total_s = 0
    total_m = 1

    for i in num_list:
        total_s += i
        total_m *= i

    if total_m > pow(total_s, 2):
        answer = 0
    else:
        answer = 1
    
    return answer