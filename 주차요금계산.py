import math
def convert(s):
    s = s.split(':')
    hour = int(s[0])
    minutes = int(s[1])
    return hour*60 + minutes
def solution(fees, records):
    answer = []  
    cars = {}
    for r in records:
        time,plate,state = r.split()
        time = convert(time)
        if state == 'IN':
            if plate not in cars:
                cars[plate] = [time,0,1]
            else:
                t,total,s = cars[plate]
                cars[plate] = [time,total,1]
        else:
            t,total,s = cars[plate]
            total += (time-t)
            cars[plate] = [0,total,0]
    costs = []
    for k,v in cars.items():
        t,total,s = cars[k]
        if s == 1:
            time = convert("23:59")
            total += (time-t)
            cars[k] = [0,total,0]
        # 기본시간 빼주고 기본요금 계산
        time = total-fees[0]
        cost = fees[1]
        # 기본 시간 제외하고도 남아있는 시간이 있다면...
        if time > 0:
            cost += (math.ceil(time/fees[2]))*fees[3]
        costs.append([k,cost])
    costs.sort()
    for plate,cost in costs:
        answer.append(cost)
    return answer
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))