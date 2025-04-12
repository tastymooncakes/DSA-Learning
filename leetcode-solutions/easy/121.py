class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0
        for i in prices:
            if low > i:
                low = i
            profit = i - low

            if profit > max_profit:
                max_profit = profit
        return max_profit