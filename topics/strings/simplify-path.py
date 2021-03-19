class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        path = path.strip('/')
        arr = path.split('/')
        print(arr)
        for p in arr:
            if p == '..':
                if result:
                    result.pop()
            elif p == '.':
                pass
            elif p != '':
                result.append(p)
        return '/'+'/'.join(result)
