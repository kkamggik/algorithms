n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]
costs = [0] * (n+1)
curr_date = len(schedules)-1
for dur, cost in schedules[::-1]:
    if(curr_date + dur <= n):
        costs[curr_date] = max(costs[curr_date + 1], costs[curr_date+dur] + cost)
    else: costs[curr_date] = costs[curr_date + 1]
    curr_date -= 1
print(max(costs))
