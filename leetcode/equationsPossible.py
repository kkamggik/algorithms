class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent = [i for i in range(26)]
        def find(x):
            if x==parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            a = find(x)
            b = find(y)
            if a < b:
                parent[a] = b
            else:
                parent[b] = a
        for a,b,c,d in equations:
            if b=='=': union(ord(a)-97, ord(d)-97)
        for a,b,c,d in equations:
            if b == '!':
                if find(ord(a)-97)==find(ord(d)-97): return False
        return True
        