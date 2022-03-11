def solution(msg):
    msg = msg.lower()
    answer = []
    dic = {}
    cnt = 1
    for i in range(26):
        dic[chr(i+97)] = cnt
        cnt += 1
    idx = 0
    tmsg = ''
    while idx < len(msg):
        tmsg += msg[idx]
        if tmsg not in dic:
            answer.append(dic[tmsg[:-1]])
            dic[tmsg] = cnt
            cnt += 1   
            tmsg = ''
            idx -= 1
        idx += 1 
    answer.append(dic[tmsg])
    return answer