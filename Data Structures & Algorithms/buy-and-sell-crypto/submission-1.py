class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        days = len(prices)

        while sell < days:
            if prices[buy] > prices[sell]:
                buy = sell
            curr_profit = prices[sell] - prices[buy]
            max_profit = max(curr_profit, max_profit)
            sell += 1
        return max_profit