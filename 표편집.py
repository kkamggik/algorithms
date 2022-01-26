from collections import defaultdict
def solution(n, k, cmd):
    answer = ['O']*(n+1)
    nodes = defaultdict(list)
    for i in range(1,n+1):
        nodes[i].append(i-1)
        nodes[i].append(i+1)
    deleted = []
    curr = k+1
    for c in cmd:
        cm = c.split(' ')
        if cm[0] == 'D': #down
            for i in range(int(cm[1])):
                curr = nodes[curr][1]
        elif cm[0] == 'U': #up
            for i in range(int(cm[1])):
                curr = nodes[curr][0]
        elif cm[0] == 'C': #delete
            answer[curr] = 'X'
            prev = nodes[curr][0]
            nxt = nodes[curr][1]
            deleted.append([curr, prev, nxt])
            if prev == 0: 
                nodes[nxt][0] = 0
                curr = nxt
            elif nxt == n+1:
                nodes[prev][1] = n+1
                curr = prev
            else:
                nodes[prev][1] = nxt
                nodes[nxt][0] = prev
                curr = nxt
        elif cm[0] == 'Z': #undo
            v,prev,nxt = deleted.pop()
            answer[v] = 'O'
            if prev == 0:
                nodes[nxt][0] = v
            elif nxt == n+1:
                nodes[prev][1] = v
            else:
                nodes[prev][1] = v
                nodes[nxt][0] = v
    return answer
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))