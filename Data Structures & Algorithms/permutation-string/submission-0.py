class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        targetHash = {}
        for char in s1:
            if char not in targetHash:
                targetHash[char] = 1
            else:
                targetHash[char] += 1

        right = 0
        
        currentHash = {}
        for left in range(len(s2)-len(s1) + 1):
            
            #build initial len(s1) set
            while right-left < len(s1):
                if s2[right] not in currentHash:
                    currentHash[s2[right]] = 1
                else:
                    currentHash[s2[right]] += 1
                right += 1
            
            if targetHash == currentHash:
                return True
            elif currentHash[s2[left]] == 1:
                del currentHash[s2[left]]
            else:
                currentHash[s2[left]] -= 1 
        return False

            

