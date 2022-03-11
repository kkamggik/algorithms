s = input()
ans = len(s)
for i in range(1,len(s)//2 + 1):
    com = ''
    prev = s[0:i]
    cnt = 1
    for j in range(i, len(s), i):
        if prev == s[j:j+i]:
            cnt += 1
        else:
            com += str(cnt)+prev if cnt >= 2 else prev
            cnt = 1
            prev = s[j:j+i]
    com += str(cnt)+prev if cnt >= 2 else prev
    ans = min(len(com), ans)
print(ans)
