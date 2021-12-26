prime = [True]*(1000001)
prime[1] = False
for i in range(2,1000001):
    for j in range(i+i,1000001,i):
        prime[j] = False
n,m = map(int, input().split())
for i in range(n,m+1):
    if prime[i]==True:
        print(i)