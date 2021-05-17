class TrieNode:
    def __init__(self, val=0):
        self.children = [None]*26
        self.endOfWord = False
        self.val = val
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str, val: int, prev:int=0) -> None:
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
            iter.val += val
            iter.val -= prev
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
                return 0
            iter = iter.children[idx]
        return iter.val if iter != None else 0

class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.words = {}
        

    def insert(self, key: str, val: int) -> None:
        if self.words.get(key, None) is not None:
            self.trie.insert(key, val, self.words.get(key))
            self.words[key] = val
        else:
            self.words[key] = val
            self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.startsWith(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
