class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0
        start, end = 0, len(height)-1
        while start < end:
            answer = max(answer, (end-start)*min(height[end],height[start]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return answer
            