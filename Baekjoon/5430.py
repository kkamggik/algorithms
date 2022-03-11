from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    t = input().strip()
    queue = deque()
    for i in t[1:-1].split(','):
        queue.append(i)
    p = p.replace('RR','')
    ans = ''
    rev = 0
    for i in p:
        if i=='R': 
            rev = (rev+1)%2
        else:
            if queue and queue[0]!='':
                if rev == 0: queue.popleft()
                else: queue.pop()
            else:
                ans = 'error'
                break
    if ans=='error': print(ans)
    else:
        ans = '['
        if rev == 0: ans += ','.join(queue)
        else: 
            queue.reverse()
            ans += ','.join(queue)
        ans += ']'
        print(ans)
