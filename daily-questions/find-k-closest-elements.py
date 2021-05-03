class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = 0
        try:
            idx = arr.index(x)
            lptr = idx
        except:
            arr.append(x)
            arr.sort()
            idx = arr.index(x)
            lptr = idx-1
        res_right = []
        res_left = []
        rptr = idx+1
        while len(res_left)+len(res_right) < k:
            if lptr >= 0 and rptr < len(arr):
                if abs(arr[lptr]-x) <= abs(arr[rptr]-x):
                    res_left.append(arr[lptr])
                    lptr -= 1
                else:
                    res_right.append(arr[rptr])
                    rptr += 1
            elif lptr >= 0:
                res_left.append(arr[lptr])
                lptr -= 1
            else:
                res_right.append(arr[rptr])
                rptr += 1
        res_left.reverse()
        return res_left+res_right
