#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)
from typing import List


def surface_area(A: List[List[int]]) -> int:
    height = len(A)
    width = len(A[0])
    area = 2 * height * width
    for i in range(height):
        for j in range(width):
            cubes = A[i][j]
            if j == 0:
                area += cubes
            if i == 0:
                area += cubes
            if i == height - 1:
                area += cubes
            if j == width - 1:
                area += cubes
            if j < width-1:
                area += abs(A[i][j + 1] - A[i][j])
            if i < height-1:
                area += abs(A[i + 1][j] - A[i][j])
    #
    # for i in range(height):
    #     for j in range(width - 1):
    #         area += abs(A[i][j + 1] - A[i][j])
    # for j in range(width):
    #     for i in range(height - 1):
    #         area += abs(A[i + 1][j] - A[i][j])
    return area


print(surface_area([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))
