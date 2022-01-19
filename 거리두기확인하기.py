dirc = [[1,0],[-1,0],[0,1],[0,-1]]
def check_surrounding(x,y):
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<5 and 0<=ny<5 and place[ny][nx]=='P': return False
def check_near(x,y):
    people = 0
    for d in dirc:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<5 and 0<=ny<5 and place[ny][nx]=='P': people += 1
    if people > 1: return False
def check():
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P': 
                if check_surrounding(j,i) == False: return False
            elif place[i][j]=='O':
                if check_near(j,i) == False: return False
    return True
def solution(places):
    answer = []
    global place
    for p in places:
        place = p[:]
        if check() == True: answer.append(1)
        else: answer.append(0)
    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))