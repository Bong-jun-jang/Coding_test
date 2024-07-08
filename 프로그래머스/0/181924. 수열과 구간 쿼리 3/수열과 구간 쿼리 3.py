def solution(arr, queries):
    answer = []
    # for i in range(len(queries)):
    #     temp = arr[queries[i][0]]
    #     arr[queries[i][0]] = arr[queries[i][1]]
    #     arr[queries[i][1]] = temp
    #     answer = arr
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
        answer = arr
    return answer