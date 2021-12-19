n = int(input())
stages = list(map(int, input().split()))
stages.sort()
ans = []
left = len(stages)
for i in range(1,n+1):
    cnt = stages.count(i)
    if left == 0:
        fail = 0
    else:
        fail = cnt/left
        left -= cnt
    ans.append([fail, i])
ans.sort(key=lambda x:(-x[0],x[1]))
for i in ans:
    print(i[1])