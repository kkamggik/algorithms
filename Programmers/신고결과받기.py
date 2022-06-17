def solution(id_list, report, k):
    names = {}
    for idx,name in enumerate(id_list):
        names[name] = idx
    n = len(id_list)
    reports = [[0]*n for _ in range(n)]
    for r in report:
        r1,r2 = r.split(' ')
        reports[names[r2]][names[r1]] = 1
    rst = [0]*n
    for i in range(n):
        if sum(reports[i]) >= k:
            rst[i] = 1
    answer = [0]*n
    for i in range(n):
        for j in range(n):
            if reports[j][i] == 1 and rst[j] == 1:
                answer[i] += 1
    return answer