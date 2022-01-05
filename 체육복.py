def solution(n, lost, reserve):
    n_reserve = [r for r in reserve if r not in lost]
    n_lost = [l for l in lost if l not in reserve]
    for r in n_reserve:
        if r-1 in n_lost:
            n_lost.remove(r-1)
        elif r+1 in n_lost:
            n_lost.remove(r+1)
    return n-len(n_lost)
print(solution(3,[2,3],[3]))