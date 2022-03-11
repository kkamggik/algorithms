import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    minheap, maxheap = [],[]
    total = (n//10) + 1 if n%10 else (n//10)
    arr = []
    for i in range(total): arr += list(map(int, input().split()))
    answer = []
    for i in range(n):
        if i%2==0: heapq.heappush(minheap, -arr[i])
        else: heapq.heappush(maxheap, arr[i])
        while minheap and maxheap and -minheap[0] > maxheap[0]:
            x = -heapq.heappop(minheap)
            y = heapq.heappop(maxheap)
            heapq.heappush(minheap, -y)
            heapq.heappush(maxheap, x)
        if i%2==0: answer.append(-minheap[0])
    cnt = 0
    print(len(answer))
    for i in answer:
        print(i, end=' ')
        cnt += 1
        if cnt == 10: 
            print()
            cnt = 0
    if cnt!=0: print()