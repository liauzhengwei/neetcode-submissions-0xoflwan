class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit = 0
        minPrice = prices[0]

        for price in prices:
            minPrice = min(minPrice, price)

            max_Profit = max(max_Profit, price - minPrice)

        return int(max_Profit)