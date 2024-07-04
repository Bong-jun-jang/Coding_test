def solution(num_list):
    c = ""
    l = ""
    for num in num_list:
        if num % 2 == 0:
            c += str(num)
        else:
            l += str(num)

    answer = int(c) + int(l)
    return answer