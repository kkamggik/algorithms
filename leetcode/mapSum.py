class MapSum(object):

    def __init__(self):
        self.dic = {}
        self.exist = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        t = 0
        if key in self.exist:
            t = self.exist[key]
        self.exist[key] = val
        for i in range(1, len(key)+1):
            tkey = key[:i]
            if tkey not in self.dic:
                self.dic[tkey] = val
            else:
                self.dic[tkey] = self.dic[tkey] - t + val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix in self.dic: return self.dic[prefix]
        return 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)