n = int(input())
arr = list(map(int, input().split()))
boss = [[] for _ in range(n)]
for i in range(n):
    if i == 0: continue
    else: boss[arr[i]].append(i)
time = [0]*n
def call(v):
    global time
    child = []
    for colleague in boss[v]:
        call(colleague)
        child.append(time[colleague])
    if not boss[v]: child.append(0)
    child.sort(reverse=True) # 시간 제일 많이 걸리는 순으로 정렬해주긔
    estimation = [child[i]+(i+1) for i in range(len(child))]
    time[v] = max(estimation)
call(0)
print(time[0]-1)