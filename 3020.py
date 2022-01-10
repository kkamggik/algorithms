n,h = map(int, input().split())
top = [0]*(h+1)
btm = [0]*(h+1)
for i in range(n):
    t = int(input())
    if i%2:
        top[t] += 1
    else:
        btm[h-t+1] += 1
for i in range(h-1,0,-1):
    top[i] += top[i+1]
for i in range(1,h+1):
    btm[i] += btm[i-1]
ans = [0]*(h+1)
for i in range(1,h+1):
    ans[i] = top[i]+btm[i]
mn = min(ans[1:])
print(mn,ans[1:].count(mn))