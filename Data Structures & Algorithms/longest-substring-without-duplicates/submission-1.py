class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = set()
        left = 0
        right = 0

        while left < len(s):
            currentMaxLength = 0
            while right <= len(s)-1:

                if s[right] not in seen:
                    currentMaxLength += 1
                    seen.add(s[right])
                    maxLength = max(maxLength, currentMaxLength)
                    right += 1
                else:
                    while s[right] in seen:
                        seen.remove(s[left])
                        left += 1
                        currentMaxLength -= 1
            left += 1
        return maxLength
