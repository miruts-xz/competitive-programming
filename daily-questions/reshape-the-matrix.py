from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = []
        for k in range(r):
            temp = []
            for x in range(c):
                temp.append(0)
            res.append(temp)
        print("{}\n".format(repr(res)))
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n: return mat
        rptr, cptr = 0, 0
        for i in range(m):
            for j in range(n):
                if cptr < c:
                    res[rptr][cptr] = mat[i][j]
                    cptr += 1
                else:
                    rptr += 1
                    cptr = 0
                    res[rptr][cptr] = mat[i][j]
                    cptr += 1
        return res


if __name__ == "__main__":
    print(Solution().matrixReshape([[1, 2], [3, 4]], 4, 1))
