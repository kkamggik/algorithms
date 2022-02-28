class Solution(object):
    def sudoku(self, idx, board):
        if idx == 9:
            global answer
            answer = True
            return
        row = [0]*10
        column = [0]*10
        for i in range(9):
            if board[idx][i].isdigit():
                num = int(board[idx][i])
                if row[num] == 0:
                    row[num] = 1
                else: return
            if board[i][idx].isdigit():
                num = int(board[i][idx])
                if column[num] == 0:
                    column[num] = 1
                else: return
        matrix = [0]*10
        x = (idx%3)*3
        y = (idx//3)*3
        for i in range(y,y+3):
            for j in range(x,x+3):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if matrix[num] == 0:
                        matrix[num] = 1
                    else: return
        self.sudoku(idx+1, board)
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        global answer
        answer = False
        n = 9
        self.sudoku(0,board)
        return answer