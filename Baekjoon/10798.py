arr = []
mlen = 0
for _ in range(5):
    lst = list(input())
    arr.append(lst)
    mlen = max(mlen, len(lst))
ans = ''
for i in range(mlen):
    for j in range(5):
        if len(arr[j]) > i:
            ans += arr[j][i]
print(ans)