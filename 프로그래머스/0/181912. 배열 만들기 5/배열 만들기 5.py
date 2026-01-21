def solution(intStrs, k, s, l):
    answer = []
    for Str in intStrs:
        num = int(Str[s:s+l])
        if num > k:
            answer.append(num)
    return answer