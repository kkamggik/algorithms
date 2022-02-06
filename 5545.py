import sys
input = sys.stdin.readline
n = int(input())
dough, topping = map(int, input().split())
dough_cal = int(input())
toppings = []
for _ in range(n): toppings.append(int(input()))
answer = (dough_cal/dough)
toppings.sort(reverse=True)
curr_cal = dough_cal
curr_cost = dough
for i in range(n):
    curr_cal += toppings[i]
    curr_cost += topping
    cost = curr_cal/curr_cost
    if cost > answer: answer = cost
    else: break
print(int(answer))