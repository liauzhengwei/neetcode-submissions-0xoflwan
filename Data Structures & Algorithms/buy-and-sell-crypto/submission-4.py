class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(price, min_price)

            profit = price - min_price

            maxProfit = max(maxProfit, profit)

        return maxProfit
