from collections import deque
def solution(queue1, queue2):
    answer = 1e9
    s1 = sum(queue1)
    s2 = sum(queue2)
    q1 = queue1[:]+queue2[:]
    q2 = queue2[:]+queue1[:]
    n = len(q1)
    queue = deque()
    queue.append([s1,s2,0,0,0])
    s = set()
    s.add((s1,s2,0,0))
    while queue:
        t1,t2,i1,i2,res = queue.popleft()
        if t1 == t2: 
            return res
        if i1 < n and (t1-q1[i1],t2+q1[i1],i1+1,i2) not in s and (t2+q1[i1],t1-q1[i1],i2,i1+1) not in s:
            queue.append([t1-q1[i1],t2+q1[i1],i1+1,i2,res+1])
            s.add((t1-q1[i1],t2+q1[i1],i1+1,i2))
            s.add((t2+q1[i1],t1-q1[i1],i2,i1+1))
        if i2 < n and (t1+q2[i2],t2-q2[i2],i1,i2+1) not in s and (t2-q2[i2],t1+q2[i2],i2+1,i1) not in s:
            queue.append([t1+q2[i2],t2-q2[i2],i1,i2+1,res+1])
            s.add((t1+q2[i2],t2-q2[i2],i1,i2+1))
            s.add((t2-q2[i2],t1+q2[i2],i2+1,i1))
    return -1