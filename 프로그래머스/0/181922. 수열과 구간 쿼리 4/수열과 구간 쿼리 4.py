def solution(arr, queries):
    answer = []
    for [s, e, k] in queries:
        for i in range(len(arr)):
            if s <= i and i <= e and (i % k == 0):
                arr[i] += 1
    answer = arr
    return answer