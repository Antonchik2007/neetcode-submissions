class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,3], [1,5], [6,7]]
        # 
        intervals.sort(key = lambda x: x[0] )
        result = []
        for i in range(len(intervals)):
            if not result:
                result.append(intervals[i])
                continue
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1]) 
                    
            
                
        return result

                    
