def solution(friends, gifts):
    index = dict()
    # 인덱싱
    for i in range(len(friends)):
        index[friends[i]] = i

    table = [[0] * len(friends) for _ in range(len(friends))]
    gift_score_table = [[0,0,0] for _ in range(len(friends))]
    # [준 선물, 받은 선물, 선물지수]
    for gift in gifts:
        sender, reciever = gift.split()
        sender, reciever = index[sender], index[reciever]
        
        table[sender][reciever] += 1
        gift_score_table[sender][0] += 1
        gift_score_table[reciever][1] += 1

    for friend in friends:
        friend = index[friend]
        gift_score_table[friend][2] = gift_score_table[friend][0] - gift_score_table[friend][1]  

    # 받을 선물 개수 테이블
    answer = [0] * len(friends)
    for _sender in friends:
        for _reciever in friends:
            if _sender == _reciever:
                continue
            sender, reciever = index[_sender], index[_reciever]

            if table[sender][reciever] > table[reciever][sender]: # 선물을 더 많이 준 경우
                answer[sender] += 1
                continue
            if table[sender][reciever] == table[reciever][sender]: # 동점인 경우
                    if gift_score_table[sender][2] > gift_score_table[reciever][2]:
                        answer[sender] += 1
    

    return max(answer)