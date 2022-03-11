n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
cnt = 0
for i in arr:
    cnt += 1
    if cnt >= i:
        ans += 1
        cnt = 0
print(ans)
# 항상 최소한의 모험가 수 만 포함하여 그룹을 결성하게 된다
# 따라서 최대한 많은 그룹이 구성되는 방법