class Solution(object):
    def countAndSay(self, n):
        nums = "1"
        for _ in range(1,n):
            num = nums[0]
            cnt = 1
            answer = ''
            for c in nums[1:]:
                if c==num:
                    cnt += 1
                else:
                    answer += str(cnt)+num
                    cnt = 1
                    num = c
            if cnt != 0:
                answer += str(cnt)+num
            nums = answer
        return nums