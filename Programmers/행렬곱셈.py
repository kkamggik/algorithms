def solution(arr1, arr2):
    n,m = len(arr1), len(arr2[0])
    answer = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            t = 0
            for k in range(len(arr1[0])):
                t += arr1[i][k] * arr2[k][j]
            answer[i][j] = t
    return answer
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))