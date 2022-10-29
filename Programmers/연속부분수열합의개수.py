def solution(elements):
    n = len(elements)
    rst = set()
    for i in range(n-1): elements.append(elements[i])
    for i in range(1,n+1):
        for j in range(n):
            rst.add(sum(elements[j:j+i]))
    return len(rst)