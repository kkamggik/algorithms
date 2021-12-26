n,m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
rst = 0
for i in coins:
    t = m//i
    rst += t
    m -= (t*i)
print(rst)