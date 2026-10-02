class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0

        left = 0
        right = len(heights)-1

        while left<right:
            maxCurrentVolume = min(heights[left], heights[right])*(right-left)
            if maxCurrentVolume > maxVolume:
                maxVolume = maxCurrentVolume
            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1
        return maxVolume