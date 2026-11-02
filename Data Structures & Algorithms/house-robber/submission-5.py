class Solution:
    def rob(self, nums: List[int]) -> int:
       money = [0] * (len(nums)+2)

       for i in range(len(nums)-1, -1, -1):
            money[i] =  max(money[i+2]+nums[i], money[i+1])
       return money[0]
