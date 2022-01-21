def solution(s):
    answer = ''
    idx = 0
    t = ''
    for i in range(len(s)+1):
        if i==len(s):
            answer += t
            return answer
        if s[i]==' ':
            answer += t
            answer += s[i]
            idx = 0
            t = ''
            continue
        elif idx==0 and not s[i].isalpha():
            t += s[i]
        elif idx==0 and s[i].isalpha():
            t += s[i].upper()
        else:
            t += s[i].lower()
        idx += 1
print(solution("3people unFollowed me"))