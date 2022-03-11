def solution(id_list, report, k):
    rst = [0]*len(id_list)
    dic = {}
    for i in range(len(id_list)):
        dic[id_list[i]] = i
    reports = [[0]*len(id_list) for _ in range(len(id_list))]
    for r in report:
        r = r.split()
        r1,r2 = dic[r[0]], dic[r[1]]
        reports[r2][r1] = 1
    for i in range(len(id_list)):
        if sum(reports[i]) >= k:
            rst[i] = 1
    answer = [0]*len(id_list)
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            if reports[j][i]==1 and rst[j]==1:
                answer[i] += 1
    return answer