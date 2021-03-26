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
    def addToReplace(self, word: str) -> str:
        iter = self.root
        n = len(word)
        root = ""
        for i in range(n):
            idx = ord(word[i])-ord('a')
            if iter.endOfWord:
                return root
            if not iter.children[idx]:
                return word
            root += chr(ord('a')+idx)
            iter = iter.children[idx]
        return word
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        ans = []
        t = Trie()
        for r in dictionary:
            t.insert(r)
        for w in words:
            ans.append(t.addToReplace(w))
        return ' '.join(ans)
