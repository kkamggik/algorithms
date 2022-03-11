def binary(start,end,target,array):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return start
def solution(info, query):
    answer = []
    applicants = {}
    for language in ['cpp','java','python','-']:
        for position in ['backend','frontend','-']:
            for experience in ['junior','senior','-']:
                for food in ['chicken','pizza','-']:
                    applicant = language+' and '+position+' and '+experience+' and '+food
                    applicants[applicant] = []
    for i in info:
        information = i.split(' ')
        for language in [information[0],'-']:
            for position in [information[1],'-']:
                for experience in [information[2],'-']:
                    for food in [information[3],'-']:
                        applicant = language+' and '+position+' and '+experience+' and '+food
                        applicants[applicant].append(int(information[4]))
    for value in applicants.values():
        value.sort()
    print(applicants)
    for q in query:
        cnt = 0
        q = q.split(' ')
        score = int(q[-1])
        q = ' '.join(q[:-1])
        match = applicants[q]
        if match:
            idx = binary(0,len(match),score,match)
            cnt = len(match) - idx
        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))