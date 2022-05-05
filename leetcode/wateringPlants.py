class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        ans = 0
        can = capacity
        for i, x in enumerate(plants): 
            if can < x: 
                ans += 2*i
                can = capacity
            ans += 1
            can -= x
        return ans 
            