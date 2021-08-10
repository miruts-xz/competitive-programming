# Created by miruts at 8/10/2021

from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = [0 for _ in range(max(len(num1), len(num2)) + 1)]
        idx = len(ans) - 1
        for n1, n2 in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            s = ans[idx] + int(n1) + int(n2)
            ans[idx] = s % 10
            ans[idx - 1] = s // 10
            idx -= 1
        ans = list(map(str, ans))
        return ''.join(ans[1:]) if ans[0] == '0' else ''.join(ans)


if __name__ == "__main__":
    print(Solution().addStrings('123', '344'))
