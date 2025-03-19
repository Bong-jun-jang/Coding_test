def solution(name, yearning, photo):
    answer = []
    for case in photo:
        score = [] 
        for i in name:
            has = any(x == i for x in case) # true or false

            if has:
                score.append(yearning[name.index(i)])
        answer.append(sum(score))
    return answer