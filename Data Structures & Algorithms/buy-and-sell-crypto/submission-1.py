class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # sell_date = 0
        least = prices[0]
        for item in prices:
            if item<least:
                least = item
            max_profit = max(item - least, max_profit)
        return max_profit