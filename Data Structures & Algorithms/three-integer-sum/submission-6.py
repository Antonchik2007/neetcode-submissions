class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        

        if len(nums) < 3:
            return []

        nums.sort()
        left_pointer = 0
        left_pointer_ahead = 1
        right_pointer = len(nums)-1

        result = []
        while left_pointer < right_pointer-1:
            while left_pointer_ahead < right_pointer:
                if nums[left_pointer] + nums[left_pointer_ahead] + nums[right_pointer] < 0:
                    left_pointer_ahead += 1
                    continue
                elif nums[left_pointer] + nums[left_pointer_ahead] + nums[right_pointer] > 0:
                    right_pointer -= 1
                else:
                    match = [nums[left_pointer],
                     nums[left_pointer_ahead],
                    nums[right_pointer]]

                    if match not in result:
                        result.append(match)
                    left_pointer_ahead += 1
            left_pointer += 1
            left_pointer_ahead = left_pointer + 1
            right_pointer = len(nums)-1
            
        return result