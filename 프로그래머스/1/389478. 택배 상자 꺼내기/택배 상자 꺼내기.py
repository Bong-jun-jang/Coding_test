def solution(n, w, num):
    answer = 0
    change = True
    box_list = []
    box = 0
    height = 0

    for total in range((n//w)+1):
        if box == n:
            break
            
        elif change == True:
            for i in range(w):

                box += 1
                box_list.append([box,i,height])
                if box == n:
                    break

                if i == w-1:
                    height += 1
                    change = False


        elif change == False:
            for j in range(w-1,-1,-1):
                box += 1
                box_list.append([box,j,height])
                if box == n:
                    break

                if j == 0:
                    height += 1
                    change = True

    info_num = list(filter(lambda width : width[0] == num , box_list))

    answer = len([count for count in box_list if count[1] == info_num[0][1] and count[0] >= info_num[0][0]])
    return answer