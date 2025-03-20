def solution(wallpaper):
    answer = []
    lux = []
    luy = []
    rdx = []
    rdy = []

    for col in range(len(wallpaper)):
        for low in range(len(wallpaper[col])):
            if wallpaper[col][low] == "#":

                lux.append(col)
                luy.append(low)
                rdx.append(col+1)
                rdy.append(low+1)

    answer = [min(lux),min(luy), max(rdx), max(rdy)]
    return answer