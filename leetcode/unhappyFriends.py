class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        match = [[0]*n for _ in range(n)]
        for i in range(n):
            rank = 1
            for j in range(n-1):
                order = preferences[i][j]
                match[i][order] = rank
                rank += 1
        pair = {}
        for x,y in pairs:
            pair[y] = x
            pair[x] = y
        answer = set()
        for x in range(n):
            y = pair[x]
            for i in range(n):
                if i!=x and match[x][i] < match[x][y] and match[i][x] < match[i][pair[i]]:
                    answer.add(x)
        return len(answer)
                