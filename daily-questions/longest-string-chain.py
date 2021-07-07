class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key = lambda x: len(x))
        memo = [None] * (len(words) + 1)
        return self.traverse(-1, words, memo) - 1
        
    # -1
    def traverse(self, current, words, memo):
        if memo[current] != None:
            return memo[current]
        result = 0
        for i in range(current + 1, len(words)):
            pred, suc = words[current], words[i]
            if current == -1:
                pred, suc = words[i], words[i] + "a"
            
            if len(suc) - len(pred) == 0:
                continue
            if len(suc) - len(pred) > 1:
                break
            if self.check(pred, suc):
                result = max(result, self.traverse(i, words, memo))
                
        memo[current] = result + 1
        return memo[current]
    
    def check(self, word1, word2):
        i = j = 0
        while i < len(word1):
            if word1[i] != word2[j] and j == i + 1:
                return False
            if word1[i] == word2[j]:
                i += 1
            j += 1
        return True
if __name__ == "__main__":
  print(Solution().longestStrChain(['a', 'b', 'ab', 'abcd'])))
