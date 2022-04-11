class Solution(object):
    def find(self,x,parents):
        if parents[x] == x: return x
        parents[x] = self.find(parents[x],parents)
        return parents[x]
    def union(self,x,y,parents):
        x = self.find(x,parents)
        y = self.find(y,parents)
        if x <= y:
            parents[y] = x
        else:
            parents[x] = y
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        parents = [i for i in range(n+1)]
        for i in range(n):
            for j in range(n):
                if i==j: continue
                if isConnected[i][j] == 1:
                    self.union(i+1,j+1,parents)
        for i in range(1,n+1):
            parents[i] = self.find(i,parents)
        counter = Counter(parents[1:])
        return len(counter)