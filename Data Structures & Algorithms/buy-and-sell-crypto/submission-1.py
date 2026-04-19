class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        left, right = 0, 1
        n = len(prices) - 1

        while right <= n:
            currentProfit = prices[right] - prices[left]
            result = max(currentProfit, result)
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
        return result