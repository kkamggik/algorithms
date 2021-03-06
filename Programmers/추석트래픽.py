def convert(date,time,duration):
    h,m,s = time.split(':')
    end = (int(h)*60*60 + int(m)*60 + float(s))*1000
    duration = float(duration[:-1])*1000
    start = end - duration + 1
    return [start,end]
def solution(lines):
    answer = 0
    timelines = []
    for line in lines:
        date,time,dur = line.split(' ')
        start,end = convert(date,time,dur)
        timelines.append([start,end])
    # 배열은 끝나는 순서대로 이미 정렬되어있음!
    for i in range(len(timelines)):
        curr_end = timelines[i][1]
        cnt = 0
        for j in range(i,len(timelines)):
            if timelines[j][0] < curr_end + 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer
# print(solution(["2016-09-15 00:00:00.000 3s"]))
# print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))