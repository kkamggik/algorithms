t = int(input())
nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
mins = [0, 0, 1, 7, 4, 2, 0, 8, 10]
minnum = [2e9]*101
for i in range(9): minnum[i] = mins[i]
minnum[6] = 6
for i in range(9, 101):
    minnum[i] = minnum[i-2]*10 + mins[2]
    for j in range(3, 8):
        temp = minnum[i-j]*10 + mins[j]
        minnum[i] = min(minnum[i], temp)
for _ in range(t):
    n = int(input())
    maxi = '7'*(n%2)+'1'*(n//2-(n%2))
    print(minnum[n], maxi)


