class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        root = self.root
        size = len(word)
        for i in range(size):
            idx = ord(word[i])-ord('a')
            if root.children[idx]:
                root = root.children[idx]
            else:
                root.children[idx] = TrieNode()
                root = root.children[idx]
        root.eow = True

    def search(self, word: str) -> bool:
        # print(self.root)
        root = self.root
        size = len(word)
        for i in range(size):
            idx = ord(word[i])-ord('a')
            if root.children[idx]:
                root = root.children[idx]
            else:
                return False
        return root.eow

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        size = len(prefix)
        for i in range(size):
            idx = ord(prefix[i])-ord('a')
            if root.children[idx]:
                root = root.children[idx]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)