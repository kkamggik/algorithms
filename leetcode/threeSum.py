class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        n = len(nums)
        answer = set()
        for i in range(n-2):
            left, right = i+1, n-1
            if nums[i] > 0: break
            while left < right:
                summ = nums[i]+nums[left]+nums[right]   
                if summ < 0:
                    left += 1
                elif summ > 0:
                    right -= 1
                else:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        rst = []
        for ans in answer:
            a,b,c = ans
            rst.append([a,b,c])
        return rst    