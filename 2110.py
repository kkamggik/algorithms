n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
start,end = 1,houses[-1]-houses[0]
ans = 0
while start <= end:
    mid = (start+end)//2
    prev = houses[0]
    cnt = 1
    for house in houses[1:]:
        if house >= prev+mid:
            prev = house
            cnt += 1
    if cnt >= c:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)