from collections import defaultdict
answer = []
routes = defaultdict(list)
def dfs(s):
    while routes[s]:
        dfs(routes[s].pop(0))
    if not routes[s]:
        answer.append(s)
def solution(tickets):
    for dep,des in tickets:
        routes[dep].append(des)
    for key in routes.keys():
        routes[key].sort()
    dfs('ICN')
    return answer[::-1]
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]))