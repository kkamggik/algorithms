arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    idx = i
    for j in range(i+1,n):
        if arr[j] < arr[idx]:
            idx = j
    arr[i],arr[idx] = arr[idx],arr[i]
print(arr)