from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        arr = [[] for _ in range(numCourses)]
        indegree = [0]*(numCourses)
        answer = []
        for a,b in prerequisites:
            indegree[a] += 1
            arr[b].append(a)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            x = queue.popleft()
            answer.append(x)
            for n in arr[x]:
                indegree[n] -= 1
                if indegree[n] == 0: queue.append(n)
        if len(answer)!=numCourses: return []
        return answer
        
        