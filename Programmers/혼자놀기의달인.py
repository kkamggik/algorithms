visited = []
cards = []
def dfs(idx, flag):
    if(visited[idx]): return
    visited[idx] = flag
    dfs(cards[idx]-1, flag)
def solution(card):
    global visited, cards
    cards = card[:]
    visited = [0]*len(cards)
    flag = 1
    for i in range(len(cards)):
        if(visited[i]==0):
            visited[i] = flag
            dfs(cards[i]-1, flag)
            flag += 1
    counter = []
    for i in range(1, flag+1):
        counter.append(visited.count(i))
    counter.sort(reverse=True)
    return counter[0]*counter[1]