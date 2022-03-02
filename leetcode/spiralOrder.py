class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix[0])
        n = len(matrix)
        visited = [[0]*m for _ in range(n)]
        x,y,d = 0,0,0
        answer = []
        dirc = [[1,0],[0,1],[-1,0],[0,-1]]
        visited[0][0] = 1
        while True:
            answer.append(matrix[y][x])
            dx,dy = x+dirc[d][0],y+dirc[d][1]
            if not (0<=dx<m and 0<=dy<n) or visited[dy][dx]:
                d = (d+1)%4
                dx,dy = x+dirc[d][0], y+dirc[d][1]
            if not (0<=dx<m and 0<=dy<n): break
            if visited[dy][dx] == 0:
                x,y = dx,dy
                visited[y][x] = 1
            else: break
        return answer
        
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         if len(matrix) == 0:
#             return res
#         row_begin = 0
#         col_begin = 0
#         row_end = len(matrix)-1 
#         col_end = len(matrix[0])-1
#         while (row_begin <= row_end and col_begin <= col_end):
#             for i in range(col_begin,col_end+1):
#                 res.append(matrix[row_begin][i])
#             row_begin += 1
#             for i in range(row_begin,row_end+1):
#                 res.append(matrix[i][col_end])
#             col_end -= 1
#             if (row_begin <= row_end):
#                 for i in range(col_end,col_begin-1,-1):
#                     res.append(matrix[row_end][i])
#                 row_end -= 1
#             if (col_begin <= col_end):
#                 for i in range(row_end,row_begin-1,-1):
#                     res.append(matrix[i][col_begin])
#                 col_begin += 1
#         return res