class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        n,m = len(grid), len(grid[0])
        arr = [0]*(n*m)
        idx = 0
        for i in range(n):
            for j in range(m):
                arr[idx] = grid[i][j]
                idx += 1
        arr.sort()
        mid = arr[len(arr)//2]
        cnt = 0
        for i in range(n*m):
            if arr[i]<=mid and (mid-arr[i])%x==0:
                cnt += (mid-arr[i])//x
            elif arr[i]>mid and (arr[i]-mid)%x==0:
                cnt += (arr[i]-mid)//x
            else: return -1
        return cnt
                
        