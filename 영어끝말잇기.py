def solution(n, words):
    answer = [0,0]
    dic = {}
    dic[words[0]] = 1
    turn = 1
    idx = 2
    prev = words[0][-1]
    for word in words[1:]:
        if word[0] == prev and word not in dic:
            dic[word] = 1
            prev = word[-1]
        else: return [idx,turn]
        idx += 1
        if idx > n:
            idx = 1
            turn += 1
    return answer
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))