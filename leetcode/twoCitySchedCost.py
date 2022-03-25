class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x:-(x[0]-x[1]))
        answer = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                answer += costs[i][1]
            else:
                answer += costs[i][0]
        return answer