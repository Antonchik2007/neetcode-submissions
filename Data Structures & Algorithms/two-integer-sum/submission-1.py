class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevSeen = {}

        for index, number in enumerate(nums):
            if number in prevSeen:
                return [prevSeen[number], index]
            else:
                prevSeen[target-number] = index
        