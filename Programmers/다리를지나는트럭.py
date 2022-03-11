def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = []
    idx,curr,time = 0,0,0
    while idx < len(truck_weights):
        sidx = 0
        while sidx < len(stack):
            stack[sidx][1] += 1
            if stack[sidx][1] == bridge_length: 
                curr -= stack[sidx][0]
                stack.remove(stack[sidx])
            else:
                sidx += 1
        if truck_weights[idx] + curr <= weight:
            curr += truck_weights[idx] 
            stack.append([truck_weights[idx],0])
            idx += 1
        time += 1
    time += (bridge_length-stack[-1][1])
    return time