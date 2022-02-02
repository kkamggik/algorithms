n = int(input())
words = {}
txts = []
for _ in range(n):
    txt = input().strip()
    txts.append(txt)
    txtlen = len(txt)
    for t in txt:
        if t in words:
            words[t] += 10**txtlen
        else:
            words[t] = 10**txtlen
        txtlen -= 1
words = sorted(words.items(), key = lambda x:-x[1])
dic = {}
value = 9
for key,val in words:
    dic[key] = value
    value -= 1
answer = 0
for _ in range(n):
    cnt = 0
    for t in txts[_]:
        cnt = cnt*10 + dic[t]
    answer += cnt
print(answer)
