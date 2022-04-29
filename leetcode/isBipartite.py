class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(node, flag):
            for nxt in graph[node]:
                if nxt in visited:
                    if visited[nxt]!=-flag:
                        global rst
                        rst = False
                        return
                else:
                    visited[nxt] = -flag
                    dfs(nxt, -flag)   
        visited = {}
        global rst
        rst = True
        n = len(graph)
        for i in range(n):
            if i not in visited:
                visited[i] = 1
                dfs(i,1)
                if rst == False: return False
        return True