import sys
input = sys.stdin.readline
n,m = map(int, input().split())
queue = [i for i in range(1,n+1)]
arr = list(map(int, input().split()))
cnt = 0
for a in arr:
    N = len(queue)
    idx = queue.index(a)
    if idx < N-idx:
        while True:
            if queue[0] == a: 
                del queue[0]
                break
            queue.append(queue[0])
            del queue[0]
            cnt += 1
    else:
        while True:
            if queue[0] == a:
                del queue[0]
                break
            queue.insert(0,queue[-1])
            del queue[-1]
            cnt += 1
print(cnt)