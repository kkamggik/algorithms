from collections import deque
def turn_right(idx, d):
    check[idx] = d
    if idx < 4 and dic[idx][2]!=dic[idx+1][6]:
        turn_right(idx+1,-d)
    
def turn_left(idx, d):
    check[idx] = d
    if 1 < idx and dic[idx][6]!=dic[idx-1][2]:
        turn_left(idx-1,-d)

a = deque(list(input()))
b = deque(list(input()))
c = deque(list(input()))
d = deque(list(input()))
m = int(input())
dic = {1:a, 2:b, 3:c, 4:d}
for _ in range(m):
    n,d = map(int, input().split())
    check = [0]*(5)
    turn_right(n,d)
    turn_left(n,d)
    for i in range(1,5):
        if check[i]==1:
            x = dic[i].pop()
            dic[i].appendleft(x)
        elif check[i]==-1:
            x = dic[i].popleft()
            dic[i].append(x)
answer = 0
score = [0,1,2,4,8]
for val, key in dic.items():
    if key[0]=='1': answer+=score[val]
print(answer)