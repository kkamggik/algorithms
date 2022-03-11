from collections import defaultdict
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for dep,des in tickets:
        routes[dep].append(des)
    for key in routes.keys():
        routes[key].sort(reverse=True)
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    return answer[::-1]
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]))