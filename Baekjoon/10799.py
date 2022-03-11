s = input()
cnt = 0
answer = 0
idx = 0
while idx < len(s):
    if s[idx]=='(' and s[idx+1]==')':
        answer += cnt
        idx += 1
    elif s[idx]=='(':
        cnt += 1
    elif s[idx]==')':
        answer += 1
        cnt -= 1
    idx += 1
print(answer)

