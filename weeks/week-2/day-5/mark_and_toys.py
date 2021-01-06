#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft of intellectual resource.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations. Don't get too scared I'm kidding :)

def maximum_toys(prices, k):
    prices.sort()
    spent = 0
    i = 0
    count = 0
    while i < len(prices):
        if spent + prices[i] <= k:
            count += 1
            spent += prices[i]
        else:
            break
        i += 1
    return count


print(maximum_toys([5, 4, 3, 7, 8, 8, 9], 12))
