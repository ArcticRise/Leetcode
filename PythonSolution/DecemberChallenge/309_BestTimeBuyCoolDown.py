"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]


"""

from typing import List

def maxProfit( prices: List[int]) -> int:
    buy, sell, hold = inf, 0, 0
    for p in prices:
        buy = min(buy, p - hold)
        hold = sell
        sell = max(sell, p - buy)
    return sell


"""
Time : O(N)
Space: O(1)

"""