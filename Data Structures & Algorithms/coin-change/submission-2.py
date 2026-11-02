class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_ways = [float("inf")] * (amount+1)
        min_ways[0] = 0
        # 0, 1, 2, 3, 4
        for i in range(amount+1):
            for coin in coins:
                if i + coin > amount:
                    continue
                min_ways[i+coin] = min(min_ways[i+coin], min_ways[i]+1)
                
        if min_ways[-1] == float("inf"):
            return -1
        else:
            return min_ways[-1]