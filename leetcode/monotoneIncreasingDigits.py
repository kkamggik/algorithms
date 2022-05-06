class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = list(str(n))
        check = len(num)
        for i in range(len(num)-2, -1, -1):
            if num[i] > num[i+1]:
                num[i] = str(int(num[i])-1)
                check = i+1
        for i in range(check, len(num)):
            num[i] = '9'
        return int(''.join(num))