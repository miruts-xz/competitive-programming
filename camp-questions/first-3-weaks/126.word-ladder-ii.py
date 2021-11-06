#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff(str1, str2)->int:
            diff = 0
            for s1, s2 in zip(str1, str2):
                if s1 != s2 and diff:
                    return 2
                elif s1 != s2:
                    diff = 1
            return diff
        visited = set()
        visited.add(beginWord)
        ans = []
        def dfs(path):
            nonlocal ans, visited
            if path[-1] == endWord:
                if ans:
                    if len(ans[-1]) < len(path):
                        ans = [[path]]
                    elif len(ans[-1]) == len(path):
                        ans.append(path)
                else:
                    ans.append(path)
                return
            for intermediate in wordList:
                if diff(beginWord, intermediate) == 1 and intermediate not in visited:
                    visited.add(intermediate)
                    dfs(path+[[intermediate]])
                    visited.remove(intermediate)
        dfs([beginWord])
        return ans
                        
                    
            
        
                
# @lc code=end

