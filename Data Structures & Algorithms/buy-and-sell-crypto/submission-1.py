class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        maxProfit = 0
        for right in range(len(prices)):

            while prices[left] > prices[right] and left<right:
                
                left += 1
            maxProfit = max(maxProfit, prices[right]-prices[left])
        return maxProfit
    
            


