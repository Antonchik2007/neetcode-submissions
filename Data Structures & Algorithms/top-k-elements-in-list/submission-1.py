class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        count = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for key, value in count.items():
            bucket[value].append(key)
        for arr in reversed(bucket):
            for num in arr:
                if len(result) < k:
                    result.append(num)
                else:
                    return result
        
        
        return result