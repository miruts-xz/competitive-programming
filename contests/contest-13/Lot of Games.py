
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

def solve(n, k, words):
    trie = Trie()
    for w in words:
        trie.insert(w)
    can_win = False
    can_lose = False
    def can_do(root, result=True):
        if not root: return result
        for node in root.children:
            if not can_do(node, not result): return True
        return False
    
    can_win = can_do(trie.root)
    can_lose = can_do(trie.root, False)
    print(can_win,can_lose)
    if can_win and can_lose: return 'First'
    if can_win and k%2: return 'First'
    if can_lose and k%2==0: return 'First'
    return 'Second'


if __name__ == '__main__':
    n, k = map(int, input().split())
    words = []
    for _ in range(n):
        words.append(input())
    print(solve(n, k, words))