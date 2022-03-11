import sys
input = sys.stdin.readline
def calculate(ppl):
    a,b = 0,0
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if ppl[i]==1 and ppl[j]==1:
                a += arr[i][j]
            if ppl[i]==0 and ppl[j]==0:
                b += arr[i][j]
    global diff
    diff = min(diff, abs(a-b))
def team(idx,num,ppl):
    if num == n//2:
        calculate(ppl)
        return
    for i in range(idx,n):
        ppl[i] = 1
        team(i+1,num+1,ppl)
        ppl[i] = 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
diff = 1e9
lng = n//2
ppl = [0]*n
for i in range(n//4):
    ppl[i] = 1
    team(i+1,1,ppl)
    ppl[i] = 0
print(diff)