n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
if k >= n: print(0)
else:
    dist = []
    for i in range(n-1):
        dist.append(arr[i+1]-arr[i])
    dist.sort(reverse=True)
    print(sum(dist[k-1:]))