class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = s.split(' ');
        for i in range(len(answer)):
            ans = list(str(answer[i]))
            left, right = 0, len(ans)-1
            while left < right:
                ans[left], ans[right] = ans[right], ans[left]
                left += 1
                right -= 1
            answer[i] = ''.join(ans)
        return ' '.join(answer)