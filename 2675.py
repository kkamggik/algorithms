t = int(input())
for _ in range(t):
    n,s = map(str, input().split())
    ans = ''
    for i in s: ans += i*int(n)
    print(ans)