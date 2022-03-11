n = int(input())
time = [300,60,10]
answer = []
for t in time:
    answer.append(n//t)
    n %= t
if n != 0:
    answer = [-1]
for n in answer: print(n, end=' ')