def solution(my_string, is_suffix):
    answer = 0
    result = [my_string[x:] for x in range(len(my_string))]
    if is_suffix in result:
        answer = 1
    
    return answer