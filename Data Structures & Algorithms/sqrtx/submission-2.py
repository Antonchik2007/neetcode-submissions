class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 0
        right = x
        res = 0

        while left <= right:
            middle = left + (right-left) // 2

            if middle*middle > x:
                right = middle-1
            else:
                left = middle + 1
                res = middle
        return res

