def solution(n, control):

    swich = {
        "w":  1,
        "s": -1,
        "d": 10,
        "a": -10
}

    for i in control:
        n += swich[i]
        
    return n