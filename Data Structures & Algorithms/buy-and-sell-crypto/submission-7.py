class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            
            # Calculate profit, and check max profit
            if sell >= len(prices):
                break
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit
            
            sell += 1
        
        return max_profit
            