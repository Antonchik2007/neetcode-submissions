class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {} # amount : min_ways
        if amount == 0:
            return 0
        def count_ways(amount):

            if amount in cache:
                return cache[amount]
            for coin in coins:
                if amount - coin == 0:
                    return 1
            if amount < 1:
                return float("inf")
            cache[amount] = 1 + min(count_ways(amount - coin) for coin in coins)

            return cache[amount]

        res = count_ways(amount)
        if res == float("inf"):
            return -1
        else:
            return res