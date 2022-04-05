class Solution(object):
    def check_row(self,mat,turn,i):
        for j in range(3):
            if mat[i][j]!=turn: return False
        return True
    def check_col(self,mat,turn,i):
        for j in range(3):
            if mat[j][i]!=turn: return False
        return True
    def check_diag1(self,mat,turn):
        for i in range(3):
            if mat[i][i]!=turn: return False
        return True
    def check_diag2(self,mat,turn):
        idx = 2
        for i in range(3):
            if mat[i][idx]!=turn: return False
            idx -= 1 
        return True
    def check(self, mat, turn):
        for i in range(3):
            if self.check_row(mat,turn,i): return True
            if self.check_col(mat,turn,i): return True
        if self.check_diag1(mat,turn): return True
        if self.check_diag2(mat,turn): return True
        return False
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        mat = [['']*3 for _ in range(3)]
        for i in range(len(moves)):
            r,c = moves[i]
            if i%2:
                mat[r][c] = 'O'
            else:
                mat[r][c] = 'X'
            if self.check(mat,'X'): return 'A'
            if self.check(mat,'O'): return 'B'
        if len(moves)==9: return 'Draw'
        return 'Pending'
                
            