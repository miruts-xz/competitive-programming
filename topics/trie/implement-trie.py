class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        iter = self.root
        n = len(word)
        for i in range(n):
            idx = ord(word[i])-ord('a')
            if not iter.children[idx]:
                iter.children[idx] = TrieNode()
            iter = iter.children[idx]
        iter.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        iter = self.root
        n = len(word)
        for i in range(n):
            idx = ord(word[i])-ord('a')
            if not iter.children[idx]:
                return False
            iter = iter.children[idx]
        return iter != None and iter.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        iter = self.root
        n = len(prefix)
        for i in range(n):
            idx = ord(prefix[i])-ord('a')
            if not iter.children[idx]:
                return False
            iter = iter.children[idx]
        return iter != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
