n = int(input())
n = str(n)
if len(n) == 1: n = '0'+n
original = n
answer = 0
while True:
    if len(n) == 1: n = '0'+n
    summ = str(int(n[0])+int(n[-1]))
    n = n[-1]+summ[-1]
    answer += 1
    if n == original: break
print(answer)