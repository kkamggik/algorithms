from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onbridge = deque(0 for i in range(len(bridge_length)))
    while len(onbridge):
        answer += 1
        onbridge.popleft()
        if truck_weights:
            if sum(onbridge) + truck_weights[0] <= weight:
                onbridge.append(truck_weights.pop(0))
            else:
                onbridge.append(0)
    return answer