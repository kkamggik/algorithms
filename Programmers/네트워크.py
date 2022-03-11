def find(x,parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x],parents)
    return parents[x]
def union(x,y,parents):
    x = find(x,parents)
    y = find(y,parents)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x 
def solution(n, computers):
    answer = 0
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if computers[i][j] == 1:
                if find(i,parents)!=find(j,parents):
                    union(i,j,parents)
    # 연결되는 순서에 따라서 union 했을 때 부모가 안잡힐수 있음... :(
    for i in range(n):
        parents[i] = find(i,parents)
    answer = set(parents)
    return len(answer)
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))