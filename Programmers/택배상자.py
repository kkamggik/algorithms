from collections import deque
def solution(order):
    answer = 0
    queue = deque()
    for i in range(1, len(order)+1):
        queue.append(i)
    temp = []
    for i in order:
        while(queue and queue[0] < i):
                temp.append(queue[0])
                queue.popleft()
        if(queue and queue[0]==i):
            queue.popleft()
            answer += 1
        else:
            if(temp[-1] == i):
                answer += 1
                temp.pop()
            else: break
    return answer