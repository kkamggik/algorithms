def solution(info, edges):
    answer = 0
    N = len(info)
    arr = [[] for _ in range(N)]
    for e1,e2 in edges:
        arr[e1].append(e2)
    # 양의 수, 늑대의 수, 방문한 노드
    stack = [(1,0,[0])]
    while stack:
        sheep, wolf, visited = stack.pop()
        answer = max(answer, sheep)
        for curr in visited:
            for nxt in arr[curr]:
                if nxt not in visited:
                    nsheep = sheep
                    nwolf = wolf
                    if info[nxt]: nwolf+=1
                    else: nsheep += 1
                    if nwolf >= nsheep: continue
                    stack.append((nsheep, nwolf, visited+[nxt]))
    return answer
print(solution(	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))