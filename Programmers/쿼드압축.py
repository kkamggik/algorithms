answer = [0,0]
board = []
def check(x,y,n):
    flag = board[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if board[i][j] != flag: return False
    return True
def quad(x,y,n):
    if check(x,y,n) == True: 
        global answer
        answer[board[y][x]] += 1
        return
    else:
        tn = n//2
        quad(x,y,tn)
        quad(x+tn,y,tn)
        quad(x,y+tn,tn)
        quad(x+tn,y+tn,tn)
def solution(arr):
    n = len(arr)
    global board
    board = arr[:]
    quad(0,0,n)
    return answer
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))