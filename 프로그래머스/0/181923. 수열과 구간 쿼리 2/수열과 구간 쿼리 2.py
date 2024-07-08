def solution(arr, queries):
    answer = []
    for i in queries:
        result = []
        for j in range(len(arr)):
            if i[0] <= j and i[1] >= j:
                if arr[j] > i[2]:
                    result.append(arr[j])
                    result.sort()
        if not result:
            result.append(-1)
        answer.append(result[0])
    return answer

