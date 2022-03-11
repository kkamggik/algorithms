def solution(s):
    answer = ''
    if len(s)%2 == 1:
        return s[len(s)//2]
    else:
        mid = len(s)//2
        return s[mid-1]+s[mid]
    return answer
print(solution("qwer"))