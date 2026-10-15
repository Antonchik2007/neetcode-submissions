class Solution:
    def climbStairs(self, n: int) -> int:
        # [1, 1] or [2]
        # step 1 = [1]
        #step 2 = [1, 1] or [2]
        #step 3 = [1, 1, 1] or [1, 2] or [2, 1]
        #step 4 = [1, 1, 1, 1] or [1, 2, 1] or [1, 1, 2] or [2, 1, 1] or [2, 2]

        #base case numWays step1 = 1
        #base case numWays step2 = 2
        #numWays step3 = step1 + step2
        #numWays step4 = 3 + 2 = 5
        # n = 1 
        counter = 1
        memo = [0, 1]
        while counter <=n:
            temp = memo[1]
            new = memo[0] + memo[1]
            memo[0] = temp
            memo[1] = new
            counter += 1
        return memo[1]