class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_ways = [float("inf")] * (amount+1)
        min_ways[0] = 0

        for amount, ways in enumerate(min_ways):
            for coin in coins:
                if amount+coin >= len(min_ways):
                    continue
                min_ways[amount+coin] = min(min_ways[amount+coin], ways + 1)
        
        res = min_ways[-1]
        if res == float("inf"):
            return -1
        else:
            return res
            

        