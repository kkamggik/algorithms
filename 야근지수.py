import heapq
def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    for i in range(n):
        x = -heapq.heappop(heap)
        if x == 0: break
        x -= 1
        heapq.heappush(heap, -x)
    while heap:
        answer += (-heapq.heappop(heap))**2
    return answer
print(solution(4, [4, 3, 3]))