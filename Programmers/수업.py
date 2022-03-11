import heapq
def solution(schedule):
    answer = 0
    for s1 in range(4):
        for s2 in range(4):
            for s3 in range(4):
                for s4 in range(4):
                    for s5 in range(4):
                        clss = []
                        s = schedule[0][s1].split(' ')
                        for i in range(0,len(s),2):
                            t,m =  s[i+1].split(':')
                            t = int(t)
                            m = int(m)
                            t *= 60
                            if len(s) == 4: heapq.heappush(clss,[s[i], t+m, 90])
                            else:  heapq.heappush(clss,[s[i], t+m, 180])
                        s = schedule[1][s1].split(' ')
                        for i in range(0,len(s),2):
                            t,m = s[i+1].split(':')
                            t = int(t)
                            m = int(m)
                            t *= 60
                            if len(s) == 4: heapq.heappush(clss,[s[i], t+m, 90])
                            else:  heapq.heappush(clss,[s[i], t+m, 180])
                        s = schedule[2][s2].split(' ')
                        for i in range(0,len(s),2):
                            t,m = s[i+1].split(':')
                            t = int(t)
                            m = int(m)
                            t *= 60
                            if len(s) == 4: heapq.heappush(clss,[s[i], t+m, 90])
                            else:  heapq.heappush(clss,[s[i], t+m, 180])
                        s = schedule[3][s3].split(' ')
                        for i in range(0,len(s),2):
                            t,m = s[i+1].split(':')
                            t = int(t)
                            m = int(m)
                            t *= 60
                            if len(s) == 4: heapq.heappush(clss,[s[i], t+m, 90])
                            else:  heapq.heappush(clss,[s[i], t+m, 180])
                        s = schedule[4][s4].split(' ')
                        for i in range(0,len(s),2):
                            t,m = s[i+1].split(':')
                            t = int(t)
                            m = int(m)
                            t *= 60
                            if len(s) == 4: heapq.heappush(clss,[s[i], t+m, 90])
                            else:  heapq.heappush(clss,[s[i], t+m, 180])
                        d,t,dr = heapq.heappop(clss)
                        while clss: 
                            td,tt,tdr = heapq.heappop(clss)
                            if d==td and ()

    return answer
print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))