class TrieNode:
    def __init__(self):
        self.children = [None]*2
        self.endOfNum = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,num):
        cur = self.root
        size = len(num)
        for i in range(size-1, -1, -1):
            digit = num[i]
            parity = int(digit)%2
            if cur.children[parity] is None:
                cur.children[parity] = TrieNode()
            cur = cur.children[parity]
        cur.endOfNum += 1
    def delete(self, num):
        cur = self.root
        for i in range(len(num)-1, -1, -1):
            digit = num[i]
            cur = cur.children[int(digit)%2]
        cur.endOfNum -= 1
    def query(self, pattern):
        res = 0
        cur = self.root
        for i in range(len(pattern)-1, -1, -1):
            p = pattern[i]
            if cur.children[int(p)]:
                cur = cur.children[int(p)]
            else:
                break
        res += cur.endOfNum
        return res 
            
operations = [input() for _ in range(int(input()))]
ans = []
trie = Trie()
for op in operations:
    ops = op.split()
    if ops[0] == '+':
        trie.insert(ops[1].zfill(18))
    elif ops[0] == '-':
        trie.delete(ops[1].zfill(18))
    else:
        ans.append(trie.query(ops[1].zfill(18)))
print(*ans, sep='\n')
