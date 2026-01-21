def solution(my_string):
    answer = [my_string[x:] for x in range(len(my_string))]
    answer.sort()
    return answer