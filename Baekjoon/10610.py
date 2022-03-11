s = list(map(str, input()))
s.sort(reverse=True)
sum = 0
for i in s:
    sum += int(i)
if sum%3!=0 or s[-1]!='0':
    print(-1)
else:
    print(''.join(s)) 