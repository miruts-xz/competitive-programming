class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        n = len(A)
        A.sort()
        rem = K
        i = 0
        while rem > 0:
            if A[i] < 0:
                A[i] *= -1
                rem -= 1
                i += 1
            elif A[i] > 0 and i < n-1:
                if rem == 1:
                    A.sort()
                    A[0] *= -1
                    rem -= 1
                else:
                    A[i] *= -1
                    rem -= 1
            elif A[i] == 0 and i < n-1:
                i += 1
            if i == n-1 and rem > 0:
                A.sort()
                i = 0
        return sum(A)
