n = int(input())
dic = {}
for i in range(n):
    name,score = map(str, input().split())
    dic[name] = int(score)
new = sorted(dic.items(), key=lambda x:-x[1])
for name in new:
    print(name[0],end=' ')