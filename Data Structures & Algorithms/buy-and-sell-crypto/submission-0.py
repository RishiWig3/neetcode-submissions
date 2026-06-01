class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for count in range(len(prices)):
            for check in range(count, len(prices)):
                if (prices[check] - prices[count]) > max:
                    max = prices[check] - prices[count]
        return max