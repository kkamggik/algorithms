from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        arr = [[] for _ in range(numCourses)]
        node = [0]*numCourses
        for a,b in prerequisites:
            arr[b].append(a)
            node[a] += 1
        queue = deque()
        for i in range(numCourses):
            if node[i]==0:
                queue.append(i)
        count = 0
        while queue:
            x = queue.popleft()
            count += 1
            for n in arr[x]:
                print(n)
                node[n] -= 1
                if node[n]==0: queue.append(n)
        if count==numCourses: return True
        return False