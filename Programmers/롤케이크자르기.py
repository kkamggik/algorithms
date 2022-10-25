def solution(topping):
    right_cnt = [0]*(10001)
    left = [0]*(10001)
    l = 0
    r = len(set(topping))
    for i in topping: right_cnt[i] += 1
    answer = 0
    for i in range(len(topping)):
        right_cnt[topping[i]] -= 1
        if(left[topping[i]]==0): l += 1
        left[topping[i]] = 1
        if(right_cnt[topping[i]]==0): r -= 1
        if(l == r): answer += 1
    return answer

