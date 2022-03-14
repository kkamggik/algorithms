class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        n,m = len(image), len(image[0])
        visited = [[0]*m for _ in range(n)]
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        color = image[sr][sc]
        queue.append([sc,sr])
        visited[sr][sc] = 1
        while queue:
            x,y = queue.popleft()
            image[y][x] = newColor
            for d in dirc:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and image[ny][nx]==color:
                    visited[ny][nx] = 1
                    queue.append([nx,ny])
        return image
            