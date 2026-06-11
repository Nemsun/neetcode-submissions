class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        max_profit = 0
        while R < len(prices):
            curr_profit = prices[R] - prices[L]
            if curr_profit < 0:
                L = R
            R = R + 1
            max_profit = max(max_profit, curr_profit)

        return max_profit