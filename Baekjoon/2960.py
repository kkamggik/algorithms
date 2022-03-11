def find(k):
    prime = [True]*(n+1)
    prime[1] = False
    cnt = 0
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if prime[j] == True:
                prime[j] = False
                cnt += 1
                if cnt == k: return j
n,k = map(int, input().split())
print(find(k))