class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def combination(cnt,arr):
            if arr: res.add(tuple(arr))
            if cnt==len(tiles): return
            for i in range(len(tiles)):
                if visited[i]==0:
                    visited[i] = 1
                    arr.append(tiles[i])
                    combination(cnt+1, arr)
                    arr.pop()
                    visited[i] = 0
        res = set()
        visited = [0]*len(tiles)
        combination(0,[])
        return len(res)