import heapq
import sys
input = sys.stdin.readline
tests = int(input())
for t in range(tests):
    maxheap = []
    minheap = []
    n = int(input())
    visited = [0]*n
    for idx in range(n):
        cm = input().split()
        if cm[0] == 'I':
            x = int(cm[1])
            visited[idx] = 1
            heapq.heappush(minheap, [x,idx])
            heapq.heappush(maxheap, [-x,idx])
        elif cm[0] == 'D':
            if cm[1] == '1':
                while maxheap and visited[maxheap[0][1]]==0:
                    heapq.heappop(maxheap)
                if maxheap: 
                    val, idx = heapq.heappop(maxheap)
                    visited[idx] = 0
            elif cm[1] == '-1':
                while minheap and visited[minheap[0][1]]==0:
                    heapq.heappop(minheap)
                if minheap: 
                    val, idx = heapq.heappop(minheap)
                    visited[idx] = 0
    while maxheap and visited[maxheap[0][1]]==0:
        heapq.heappop(maxheap)
    while minheap and visited[minheap[0][1]]==0:
        heapq.heappop(minheap)
    if not maxheap and not minheap: print('EMPTY')
    else:
        print(-maxheap[0][0], minheap[0][0])