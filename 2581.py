prime = [True]*10001
for i in range(2,10001):
    for j in range(i+i, 10001, i):
        prime[j] = False
prime[1] = False
n = int(input())
m = int(input())
cnt,s,mn = 0,0,1e9
for i in range(n,m+1):
    if prime[i] == True:
        cnt += 1
        s += i
        mn = min(mn, i)
if cnt == 0: print(-1)
else:
    print(s)
    print(mn)