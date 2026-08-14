class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for character in string:
                count[ord(character) - ord("a")] += 1
            hashMap[tuple(count)].append(string)
        return list(hashMap.values())
                 



        
