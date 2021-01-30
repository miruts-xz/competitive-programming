class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        r, mn, mx, x, y = [], 1001, 0, 1, 1000
        while x <= 1000 and y >= 1:
            ans = customfunction.f(x, y)
            if ans == z:
                mn = min(mn, x, y)
                mx = max(mx, x, y)
                y -= 1
                x += 1
            if ans < z:
                x += 1
            elif ans > z:
                y -= 1
        tempMax, tempMin = mx, mn
        while mn and mn <= tempMax and mx >= tempMin:
            ans = customfunction.f(mn, mx)
            if ans == z:
                r.append([mn, mx])
                mn += 1
                mx -= 1
            elif ans < z:
                mn += 1
            else:
                mx -= 1
        return r
