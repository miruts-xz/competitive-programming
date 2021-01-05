#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)

def counting_sort_2(arr):
    if len(arr) == 0:
        return arr
    maximum = arr[0]
    for n in arr:
        if maximum < n:
            maximum = n
    a = [0] * (maximum + 1)
    for n in arr:
        a[n] += 1
    cumm = 0
    for i in range(len(a)):
        for j in range(a[i]):
            arr[cumm] = i
            cumm += 1
    return arr


print(counting_sort_2([4, 5, 6, 1, 0, 9, 4, 8]))
