prime = [True]*(1001)
prime[1] = False
for i in range(2,1001):
    for j in range(i+i, 1001, i):
        prime[j] = False
n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in lst:
    if prime[i] == True: ans += 1
print(ans)