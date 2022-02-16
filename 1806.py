n,k = map(int, input().split())
arr = list(map(int, input().split()))
s,e = 0,0
summ = 0
answer = 2e9
while True:
    if summ >= k:
        answer = min(answer, e-s)
        summ -= arr[s]
        s += 1
    elif e == n: break
    else:
        summ += arr[e]
        e += 1
print(answer)