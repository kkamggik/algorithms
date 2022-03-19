class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.dic = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.dic[self.freq[val]].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.dic[self.max_freq].pop()
        if not self.dic[self.max_freq]:
            self.max_freq -= 1
        self.freq[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()