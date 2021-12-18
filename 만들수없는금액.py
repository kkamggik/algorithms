# 만들 수 없는 양의 정수 금액 중 최솟값
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 1
for i in arr:
    if ans < i: break
    ans += i
print(ans)
    