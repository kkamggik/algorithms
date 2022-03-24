class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        cnt = 0
        start, end = 0,len(people)-1
        while start <= end:
            if people[start]+people[end] <= limit:
                cnt += 1
                start += 1
                end -= 1
            else:
                cnt += 1
                end -= 1
        return cnt