from collections import deque
def solution(people, limit):
    answer = 0 
    queue = deque()
    people.sort(reverse = True)
    for ppl in people:
        queue.append(ppl)
    while queue:
        answer += 1
        curr = queue.popleft()
        if(queue and curr + queue[-1] <= limit):
            queue.pop()
    return answer