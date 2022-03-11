from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i],i])
    order = 1
    while queue:
        x,idx = queue.popleft()
        exist = False
        for i in range(len(queue)):
            if queue[i][0] > x:
                exist = True
                break
        if exist:
            queue.append([x,idx])
        else:
            if location == idx:
                return order
            else:
                order += 1
    return answer