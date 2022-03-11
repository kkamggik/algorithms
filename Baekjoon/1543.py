import sys
input = sys.stdin.readline
word = input().strip()
target = input().strip()
idx = 0
answer = 0
while idx < len(word)-len(target)+1:
    tidx = idx
    for i in range(len(target)):
        if word[tidx] == target[i]: tidx += 1
        else: break
    if tidx == idx+len(target): 
        idx = tidx - 1
        answer += 1
    idx += 1
print(answer)