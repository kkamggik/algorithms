n = int(input())
arr = []
for _ in range(n):
    x,y = map(int, input().split())
    arr.append([x,y])
ans = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if i==j: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    ans.append(cnt+1)
for i in ans: print(i,end=' ')