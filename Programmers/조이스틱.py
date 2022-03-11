def solution(name):
    ans = 0
    dirc = len(name)-1
    for i,j in enumerate(name):
        ans += min(ord(j)-ord('A'), ord('Z')-ord(j)+1)
        nxt = i+1
        while nxt<len(name) and name[nxt]=='A':
            nxt += 1
        dirc = min(dirc, i+i+len(name)-nxt)
    return ans+dirc