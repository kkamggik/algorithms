s,e = 0,0
summ = 0
answer = 0
while True:
    if summ >= m:
        if summ==m: answer += 1
        summ -= arr[s]
        s += 1
    elif e==n: break
    else:
        summ += arr[e]
        e += 1
print(answer)