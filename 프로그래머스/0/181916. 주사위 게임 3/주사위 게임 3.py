def solution(a, b, c, d):
    answer = 0
    
    arr = [a,b,c,d]
    count = set(arr)
    count = list(count)

    if len(count) == 1:
        answer = count[0] * 1111
    elif len(count) == 2:
        if arr.count(count[0]) == 3:
            answer = pow((10*count[0] + count[1]),2)
        elif arr.count(count[1]) == 3: 
            answer = pow((10*count[1] + count[0]),2)
        else: answer = (count[0]+count[1]) * abs(count[0]-count[1])
    elif len(count) == 3:
        for i in count:
            if arr.count(i) == 2:
                count.remove(i)
                answer = count[0] * count[1]
    elif len(count) == 4:
        answer = min(count)
    
    return answer