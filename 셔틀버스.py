def convert(time):
    h,m = time.split(":")
    return int(h)*60+int(m)
def convert_time(t):
    h,m = t//60, t%60
    time = ''
    if h < 10: time = '0'
    time += str(h)+':'
    if m < 10: time += '0'
    time += str(m)
    return time
def solution(n, t, m, timetable):
    answer = -1
    order = []
    for time in timetable:
        mins = convert(time)
        order.append(mins)
    order.sort()
    buses = [9*60 + t*i for i in range(n)]
    idx = 0
    for time in buses:
        cnt = 0
        while cnt < m and idx < len(order) and order[idx] <= time:
            cnt += 1
            idx += 1
        if cnt < m: answer = time
        else: answer = order[idx-1]-1
    return convert_time(answer)
# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))