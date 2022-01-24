def solution(gems):
    answer = 1e9
    count = len(set(gems))
    gem = {}
    cnt = 0
    s,e = 0,0
    while e < len(gems):
        if gems[e] not in gem:
            gem[gems[e]] = 1
            cnt += 1
        else: gem[gems[e]] += 1
        e += 1
        if cnt == count:
            while s < e:
                if gem[gems[s]] > 1:
                    gem[gems[s]] -= 1
                    s += 1
                elif e-s < answer:
                    answer = e-s
                    rst = [s+1,e]
                    break
                else: break
    return rst
print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))