def max_profit_runner():
    weights = [1, 2, 3, 5]
    values = [1, 6, 10, 16]
    dp = {}
    def max_profit(i, cap)->int:
        nonlocal dp
        if cap <= 0 or i == len(weights): return 0
        if (i, cap) not in dp:
                dp[i, cap] = max(values[i] + max_profit(i+1, cap-weights[i]), max_profit(i+1, cap)) if weights[i] <= cap else max_profit(i+1, cap)
        return dp[i, cap]
    print(max_profit(0, 7))
max_profit_runner()