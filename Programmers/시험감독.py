n = int(input())
sites = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0
for num in sites:
    ans += 1
    if(num - b > 0):
        if(num-b)%c != 0:
            ans += 1
        ans += (num-b)//c
print(ans)
