class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1
        while left < len(prices)-1:
            if prices[left]>prices[right]:
                    left += 1
                    right = left + 1
                    continue
            while right < len(prices):
                maxProfit = max(maxProfit, prices[right]-prices[left])
                right += 1
            left += 1
            right = left+1
        return maxProfit
            


