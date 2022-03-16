class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(mat)
        m = len(mat[0])
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0: queue.append([j,i])
                else: mat[i][j] = -1
        while queue:
            x,y = queue.popleft()
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n and mat[ny][nx]==-1:
                    queue.append([nx,ny])
                    mat[ny][nx] = mat[y][x]+1
        return mat