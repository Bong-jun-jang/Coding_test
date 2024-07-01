def solution(friends, gifts):
    answer = 0
    send_gifts = []
    gift_point = []
    receive_gifts = [0] * len(friends)
    
    for i in range(len(friends)):
        give = [0] * len(friends)
        s_count = 0
        r_count = 0
        for j in range(len(gifts)):

            send, receive = gifts[j].split()
            if receive == friends[i]:
                r_count += 1
            if send == friends[i]:
                s_count += 1
                for friend in range(len(friends)):
                    if friends[friend] == receive:
                        give[friend] += 1

        gift_point.append(s_count-r_count)
        send_gifts.append(give)
    
    for i in range(len(send_gifts)):
        for j in range(len(send_gifts[i])):
            if i!=j and send_gifts[i][j] > send_gifts[j][i]:
                receive_gifts[i] += 1
            if (send_gifts[i][j] == send_gifts[j][i]) or (send_gifts[i][j] == 0 and send_gifts[j][i] == 0):
                if gift_point[i] > gift_point[j]:
                    receive_gifts[i] += 1

    answer = max(receive_gifts)
    
    return answer