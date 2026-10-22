class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = None
        for num in nums:
            if not result:
                result = num
            else:
                result = result^num
        return result
