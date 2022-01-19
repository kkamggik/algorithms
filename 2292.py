n = int(input())
answer = 1
start = 1
size = 6
while True:
    if n <= start: break
    start += size
    size += 6
    answer += 1
print(answer)