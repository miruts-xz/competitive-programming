from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, newColor, image[sr][sc])
        return image

    def fill(self, image: List[int], sr: int, sc: int, newColor, originalColor):
        image[sr][sc] = newColor
        for i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            r = sr + i[0]
            c = sc + i[1]
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == originalColor:
                self.fill(image, r, c, newColor, originalColor)
