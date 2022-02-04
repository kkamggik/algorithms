import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
stack = []
answer = 0
for i in range(m):
    if arr[i] not in stack:
        if len(stack) < n:
            stack.append(arr[i])
        else:
            pull = [-1,-1]
            for s in stack:
                if s not in arr[i+1:]:
                    pull = [-1,s]
                    break
                else:
                    idx = arr[i+1:].index(s)
                    if pull[0] < idx:
                        pull = [idx, s]
            stack.remove(pull[1])
            stack.append(arr[i])
            answer += 1
print(answer)
                
