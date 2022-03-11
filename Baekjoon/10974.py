def order(idx, lst):
    if len(lst)==n:
        for item in lst: print(item, end=' ')
        print()
        return
    for i in range(1,n+1):
        if visit[i]==0:
            visit[i] = 1
            lst.append(i)
            order(idx+1, lst)
            visit[i] = 0
            lst.pop()
n = int(input())
visit = [0]*(n+1)
order(1,[]) 