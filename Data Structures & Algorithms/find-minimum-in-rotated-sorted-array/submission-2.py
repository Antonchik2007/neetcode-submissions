class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        minElement = float("inf")

        if len(nums) == 1:
            return nums[0]
        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                minElement = min(minElement, nums[right])
                left = middle + 1
            else:
                minElement = min(minElement, nums[middle])
                right = middle
        return minElement