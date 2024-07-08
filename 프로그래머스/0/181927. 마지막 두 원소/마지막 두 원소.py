def solution(num_list):
    answer = []
    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
        answer = num_list
    elif num_list[-1]<=num_list[-2]:
        num_list.append(num_list[-1]*2)
        answer = num_list
    return answer