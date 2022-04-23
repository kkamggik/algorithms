class MyHashMap(object):

    def __init__(self):
        self.dic = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.dic[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic and self.dic[key]!=None: return self.dic[key]
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.dic: self.dic[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)