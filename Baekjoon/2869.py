a,b,v = map(int, input().split())
nv = v-a
h = a-b
answer = (nv//h) + 1
if nv%h:
    answer += 1
print(answer)