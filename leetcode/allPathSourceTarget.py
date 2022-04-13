class Solution(object):
    def dfs(self, idx, arr, graph):
        global res, visited
        if idx == len(graph)-1:
            res.append(arr[:])
            return
        for n in graph[idx]:
            if visited[n]==0:
                visited[n] = 1
                self.dfs(n,arr+[n],graph)
                visited[n] = 0
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        global res, visited
        visited = [0]*len(graph)
        res = []
        visited[0] = 1
        self.dfs(0,[0],graph)
        return res