n = int(input())
rst = 0
for _ in range(n):
    s = input()
    alp = [0]*26
    alp[ord(s[0])-ord('a')] = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]: continue
        else:
            if alp[ord(s[i])-ord('a')] == 1:
                cnt = 0
                break
            else:
                alp[ord(s[i])-ord('a')] = 1
    rst += cnt
print(rst)