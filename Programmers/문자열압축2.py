def solution(s):
    answer = 2e9
    n = len(s)//2
    for i in range(1, n+1):
        start = s[:i]
        t = ''
        cnt = 0
        for j in range(0, len(s), i):
            if(start == s[j:j+i]):
                cnt += 1
            else:
                if(cnt > 1): t += (str(cnt) + start)
                else: t += start
                start = s[j:j+i]
                cnt = 1
        if(cnt == 1): t += start
        else: t += (str(cnt) + start)
        answer = min(answer, len(t))
    if(len(s)==1): answer = 1
    return answer
