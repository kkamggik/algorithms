class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        parent = [i for i in range(n)]
        def find(x):
            if parent[x]==x: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            x = find(x)
            y = find(y)
            if x > y: parent[x] = y
            else: parent[y] = x
        for a,b in pairs:
            union(a,b)
        dic = defaultdict(list)
        for i in range(n):
            dic[find(i)].append(s[i])
        for key in dic.keys():
            dic[key].sort(reverse=True)
        res = ''
        for i in range(n):
            res += dic[find(i)].pop()
        return res

        