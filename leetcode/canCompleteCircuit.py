class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas): return -1
        n = len(gas)
        summ, start = 0,0
        for i in range(n):
            summ += gas[i] - cost[i]
            if summ < 0:
                summ = 0
                start = i+1
        if start > n: return -1
        return start
            
                
            
        