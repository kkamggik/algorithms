prime = [True]*(246913)
prime[1] = False
for i in range(2, 246913):
    for j in range(i+i, 246913, i):
        prime[j] = False
while True:
    n = int(input())
    if n==0: break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if prime[i]==True: cnt+=1
    print(cnt)