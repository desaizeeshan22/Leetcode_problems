# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    curr_min = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        curr_min = min(prices[i], curr_min)
        max_profit = max(max_profit, prices[i] - curr_min)
    return max_profit

