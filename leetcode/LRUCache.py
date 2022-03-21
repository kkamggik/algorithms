class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = OrderedDict()
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic: return -1
        val = self.dic.pop(key)
        self.dic[key] = val
        return val
 
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic: self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
