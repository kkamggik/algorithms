import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >=2 and scoville[0] < K:
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x+2*y)
        answer += 1
    if scoville[0] < K: return -1
    return answer