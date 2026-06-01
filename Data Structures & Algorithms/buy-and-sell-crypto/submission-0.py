class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buy = prices[0]
        for i in range(len(prices)):
            curr_profit = prices[i] - best_buy
            max_profit = max(curr_profit, max_profit)
            if (prices[i] < best_buy):
                best_buy = min(prices[i], best_buy)
        return max_profit