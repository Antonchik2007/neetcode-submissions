class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashMap = {}
        maxLength = 0
        left = 0
        for right in range(len(s)):

            if s[right] not in hashMap:
                hashMap[s[right]] = 1
            else:
                hashMap[s[right]] += 1

            while (right - left + 1) - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right-left+1)
        return maxLength
            

        
                
                
            







            