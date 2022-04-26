class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def find(x):
            if parent[x]==x: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            x = find(x)
            y = find(y)
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
        n = len(points)
        parent = [i for i in range(n)]
        arr = []
        for i in range(n):
            for j in range(i+1,n):
                d = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                arr.append([d,i,j])
        arr.sort(key = lambda x:x[0])
        res = 0
        for d,a,b in arr:
            if find(a)!=find(b):
                union(a,b)
                res += d
        return res