from collections import defaultdict
answer = []
arr = list(map(int, input().split()))
dic = defaultdict(int)
for n in arr:
    dic[n] += 1
for k,v in dic.items():
    for i in range(v//3): answer.append(k)
print(answer)
