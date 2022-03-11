import heapq
def solution(jobs):
    answer = []
    heap = []
    for s,d in jobs:
        heapq.heappush(heap, [s,d])
    now = 0
    while heap:
        tmp = []
        while heap and heap[0][0] <= now:
            x,y = heapq.heappop(heap)
            heapq.heappush(tmp,[y,x])
        if tmp:
            y,x = heapq.heappop(tmp)
            now += y
            answer.append(now-x)
            while tmp:
                y,x = heapq.heappop(tmp)
                heapq.heappush(heap,[x,y])
        else:
            now += 1
    return sum(answer)//len(answer)
print(solution([[0, 3], [4, 3], [7, 3]]))