def solution(sizes):
    ra,rb = 0,0
    for a,b in sizes:
        if a > b:
            a,b = b,a
        ra = max(ra, a)
        rb = max(rb, b)
    return ra*rb