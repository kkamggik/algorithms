from collections import deque
table = []
arr = []
def profit(cost, idx):
    queue = deque()
    queue.append([idx, cost])
    while queue:
        idx, cost = queue.popleft()
        if idx==0 or cost==0: return
        tcost = cost//10
        table[idx] += (cost - tcost)
        queue.append([arr[idx],tcost])
def solution(enroll, referral, seller, amount):
    global table, arr
    answer = []
    n = len(enroll)
    name = {}
    for i in range(n):
        name[enroll[i]] = i+1
    arr = [0]*(n+1)
    for i in range(n):
        if referral[i] == '-':
            arr[i+1] = 0
        else:
            arr[i+1] = name[referral[i]]
    table = [0]*(n+1)
    for i in range(len(seller)):
        s = name[seller[i]]
        profit(amount[i]*100, s)
    return table[1:]
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))