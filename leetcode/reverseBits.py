class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        answer = 0
        for i in range(32):
            answer = (answer << 1) ^ (n & 1)
            n = n >> 1
        return answer