n = int(input())
mts = []
for _ in range(n):
    a,b = map(int, input().split())
    mts.append([a,b])
mts.sort(key = lambda x:(x[1],x[0]))
end = mts[0][1]
cnt = 1
for i,j in mts[1:]:
    if end <= i:
        cnt += 1
        end = j
print(cnt)