def solution(participant, completion):
    dic = {}
    for part in participant:
        if part in dic:
            dic[part] += 1
        else:
            dic[part] = 1
    for com in completion:
        if com not in dic:
            return com
        else:
            if dic[com] >= 1:
                dic[com] -= 1
            else:
                return com
    for key in dic:
        if dic[key] >= 1: return key
    return answer
