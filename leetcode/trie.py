class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.isEnd = True
        
    def search(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char)
            if not current: return False
        return current.isEnd
        
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if not current: return False
        return True