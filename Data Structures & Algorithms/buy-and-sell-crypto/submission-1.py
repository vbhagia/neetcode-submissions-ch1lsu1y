class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We want to maximize profit
        # This means price sold - price bought must be maximized
        # I'll do a brute force (O(n^2)) approach my first pass
        max_profit = 0 # var to store cur_max
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        if max_profit < 0:
            max_profit = 0
        return max_profit