def solution(s, n):
    s = list(s)
    cnt = 0
    for i in range(len(s)-1):
        alp = ord(s[i])
        idx = -1
        for j in range(i+1,len(s)):
            if(ord(s[j]) > alp):
                alp = ord(s[j])
                idx = j
        if(cnt < n and alp != ord(s[i])):
            t = s[i]
            s[i] = s[idx]
            s[idx] = t
            cnt += 1
        else: break
    answer = "".join(s)
    return answer
print(solution("aabb", 3))