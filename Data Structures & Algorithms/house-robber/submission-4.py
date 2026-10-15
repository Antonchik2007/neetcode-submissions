class Solution:
    def rob(self, nums: List[int]) -> int:
        
        total = [0] * (len(nums)+2)

        for i in range(len(nums)-1, -1, -1,):
            total[i] = max(nums[i] + total[i+2], total[i+1])
        return total[0]

        