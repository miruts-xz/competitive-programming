import sys
sys.setrecursionlimit(10**9)
class TrieNode:
    def __init__(self):
        self.children = [None]*3
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

def has_match(root, querry, index, availed=False)->bool:
    if index == len(querry) or not root: return availed
    if availed:
        for char in querry:
            idx = ord(char)-ord('a')
            if root.children[idx]:
                root = root.children[idx]
            else:
                return False
        return root.eow
    idx = ord(querry[index])-ord('a')
    if index == len(querry)-1:
        for i, new in enumerate(root.children):
            if new and i != idx and new.eow:
                return True
        return False
    has = False
    for j, newroot in enumerate(root.children):
        if has:
            return has
        if not newroot: continue
        has = has_match(newroot, querry, index+1, True if j != idx else False)
    return has
ans = []
if __name__ == '__main__':
    n, m = map(int, input().split())
    trie = Trie()
    for _ in range(n):
        trie.insert(input())
    for _ in range(m):
        ans.append('YES' if has_match(trie.root, input(), 0) else 'NO')
print(*ans, sep='\n')