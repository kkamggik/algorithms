from collections import deque
def solution(people, limit):
    answer = 0
    queue = deque()
    people.sort(reverse=True)
    for p in people:
        queue.append(p)
    answer = 0
    while queue:
        answer += 1
        x = queue.popleft()
        if queue and x+queue[-1] <= limit:
            queue.pop()
    return answer
print(solution([100,500,500,900,950], 1000))