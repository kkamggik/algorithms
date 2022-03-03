class Solution(object):
    global dirc
    dirc = [[1,0],[-1,0],[0,1],[0,-1]]
    def dfs(self, x, y, idx, word, board,n,m):
        if idx == len(word):
            global answer
            answer = True
            return
        for d in dirc:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and board[ny][nx]==word[idx]:
                visited[ny][nx] = 1
                self.dfs(nx,ny,idx+1,word,board,n,m)
                visited[ny][nx] = 0
            
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        global answer, visited
        answer = False
        n = len(board)
        m = len(board[0])
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and answer == False:
                    visited[i][j] = 1
                    self.dfs(j,i,1,word,board,n,m)
                    visited[i][j] = 0
        return answer