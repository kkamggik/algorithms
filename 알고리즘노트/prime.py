prime = [True]*10001
for i in range(2,10001):
    for j in range(i+i, 10001, i):
        prime[j] = False