coins = [25, 10, 5, 1]
answer = [0,0,0,0]
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(4):
        answer[i] = n//coins[i]
        n %= coins[i]
    for i in answer:
        print(i, end=' ')
    print()