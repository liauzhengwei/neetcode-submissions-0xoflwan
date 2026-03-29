class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price

            maxProfit = max(maxProfit, profit)

        return maxProfit
