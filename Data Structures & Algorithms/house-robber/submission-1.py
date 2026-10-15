class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2, 3, 6, 4, 5, 40] -> [2, 6, 40]
        # rob || skip
        # rob -> n+2
        # skip -> n+1
        # rob<skip : rob(n+1) else nums[i] + rob(n+2)
        # total + n+1 vs total + curr
        # [1, 1, 3, 3]
        total = [0]*(len(nums)+2) # {index: (rob, skip)}
        for i in range(len(nums)-1, -1, -1):
            if total[i]:
                return max(nums[i]+total[i+1], total[i])
            else:
                total[i] = max(nums[i] + total[i+2], total[i+1])
        return total[0]
                

        