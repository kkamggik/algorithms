import heapq
def solution(operations):
    heap = []
    for operation in operations:
        cm = operation.split(' ')
        if cm[0] == 'I':
            heapq.heappush(heap, int(cm[1]))
        elif cm[0] == 'D':
            if cm[1] == '1' and heap:
                tmp = []
                idx = 0
                while heap:
                    heapq.heappush(tmp, heapq.heappop(heap))
                while idx < len(tmp)-1:
                    heapq.heappush(heap, heapq.heappop(tmp))
            elif cm[1] == '-1' and heap:
                heapq.heappop(heap)
    if not heap: return [0,0]
    answer = [0,0]
    answer[0] = heapq.heappop(heap)
    answer[1] = answer[0]
    while heap:
        answer[0] = heapq.heappop(heap)
    return answer
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))