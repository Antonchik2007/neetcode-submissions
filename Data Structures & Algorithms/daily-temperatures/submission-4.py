class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 22 21 23
        # 22 < 23 ; index[23] - index[22] ; index[23] - index[21]
        waiting_list = [] #(temp, index)
        result = [0] * len(temperatures) #

        for index, temp in enumerate(temperatures):
            if not waiting_list:
                waiting_list.append((temp, index))
            while waiting_list and temp > waiting_list[-1][0]:
                result[waiting_list[-1][1]] = index-waiting_list[-1][1]
                waiting_list.pop()
            waiting_list.append((temp, index))
        return result
        


