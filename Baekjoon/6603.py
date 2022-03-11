import sys
input = sys.stdin.readline
def dfs(rst,idx):
    if 6 == len(rst):
        for num in rst:
            print(num,end=' ')
        print()
        return
    for i in range(idx,len(lst)):
        rst.append(lst[i])
        dfs(rst,i+1)
        rst.pop()
while True:
    lst = list(map(int, input().split()))
    if len(lst)==1 and lst[0]==0: break
    lst = lst[1:]
    rst = []
    for i in range(len(lst)-5):
        rst.append(lst[i])
        dfs(rst,i+1)
        rst.pop()
    print()