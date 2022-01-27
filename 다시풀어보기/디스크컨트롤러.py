import heapq
def solution(jobs):
    answer = []
    heap = []
    for job in jobs:
        heapq.heappush(heap,[job[0],job[1]])
    curr = 0
    while heap:
        temp = []
        # 시작시간이 현재시간보다 작은 작업들 빨리 끝나는 순서대로
        while heap and heap[0][0] <= curr:
            s,e = heapq.heappop(heap)
            heapq.heappush(temp,[e,s])
        if temp:
            e,s = heapq.heappop(temp)
            answer.append(curr-s+e)
            curr += e
            while temp:
                e,s = heapq.heappop(temp)
                heapq.heappush(heap,[s,e])
        else: curr += 1
    return sum(answer)//len(answer)
print(solution(	[[0, 3], [1, 9], [2, 6]]))