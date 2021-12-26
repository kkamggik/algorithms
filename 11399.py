n = int(input())
arr = list(map(int, input().split()))
queue = []
for i in range(1,n+1):
    queue.append([arr[i-1],i])
queue.sort()
sum = 0
tmp = 0
for i,j in queue:
    tmp += i
    sum += tmp
print(sum)