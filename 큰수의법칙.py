n,m,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
first = arr[0]
second = arr[1]
count = int(m/(k+1))*k
count += m%(k+1)
ans = 0
ans += (count)*first
ans += (m-count)*second
print(ans)