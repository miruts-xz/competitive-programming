#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)

def find_median(arr):
    arr.sort()
    return arr[len(arr) // 2]


print(find_median([1, 4, 3, 9, 6, 7, 6]))
