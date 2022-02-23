from collections import defaultdict
def lengthOfLongestSubstring(s):
    alp = defaultdict(int)
    start,end = 0,0
    cnt, answer = 0,0
    while end < len(s):
        c = ord(s[end])
        if alp[c]!=1:
            alp[c] = 1
            end += 1
            cnt += 1
            answer = max(answer, cnt)
        else:
            c = ord(s[start])
            alp[c] = 0
            start += 1
            cnt -= 1
    return answer
print(lengthOfLongestSubstring("pwwkew"))