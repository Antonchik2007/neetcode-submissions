class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLength = 1
        prevSeen = {}
        # number : count
        for number in nums:
            if number not in prevSeen:
                prevSeen[number] = 1
            else:
                prevSeen[number] += 1
        for number in nums:
            maxSeen = 1
            if number-1 not in prevSeen:  
                index = 1
                while number+index in prevSeen:
                    maxSeen += 1
                    index += 1
            if maxSeen>maxLength:
                maxLength = maxSeen
        return maxLength
            