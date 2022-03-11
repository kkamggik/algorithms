def check(rst):
    for x,y,a in rst:
        if a == 0: # 기둥
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            if y != 0 and (x,y-1,0) not in rst and (x-1,y,1) not in rst and (x,y,1) not in rst: return False
        else: # 보
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if (x,y-1,0) not in rst and (x+1,y-1,0) not in rst and not((x+1,y,1) in rst and (x-1,y,1) in rst): return False
    return True
def solution(n, build_frame):
    rst = set()
    for x,y,a,b in build_frame:
        item = (x,y,a)
        if b: # build
            rst.add(item)
            if not check(rst): rst.remove(item)
        elif item in rst:
            rst.remove(item)
            if not check(rst): rst.add(item)
    answer = []
    for a,b,c in rst: answer.append([a,b,c])
    answer.sort()
    return answer
print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))