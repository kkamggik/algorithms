class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = []
    def insert(self, word):
        root = self.root
        length = len(word)
        for i in range(length):
            c = ord(word[i])-ord('a')
            if not root.children[c]:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.isEnd = True
    def dfs(self, node, word):
        if len(self.res) == 3: return
        if node.isEnd:
            print(word)
            self.res.append(word)
        for i in range(26):
            if node.children[i]:
                self.dfs(node.children[i], word+chr(i+97))
    def search(self, word):
        self.res = []
        root = self.root
        length = len(word)
        for i in range(length):
            c = ord(word[i])-ord('a')
            if not root.children[c]: return []
            root = root.children[c]
        self.dfs(root, word)
        return self.res
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = Trie()
        for product in products:
            trie.insert(product)
        for i in range(1, len(searchWord)+1):
            strs = trie.search(searchWord[:i])
            print(strs)