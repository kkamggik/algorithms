import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    name, kor, eng, math = map(str, input().strip().split())
    arr.append([int(kor), int(eng), int(math), name])
arr.sort()
arr.sort(key = lambda x:(-x[0],x[1],-x[2]))
for i in range(n):
    print(arr[i][3])