t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0]*(12)
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4, 12):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    print(arr[n])
