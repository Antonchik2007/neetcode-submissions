class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_list = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if waiting_list == []:
                waiting_list.append((temp, index))
            else:
                while(waiting_list and temp>waiting_list[-1][0]):
                    result[waiting_list[-1][1]] = (index-waiting_list[-1][1])
                    waiting_list.pop()
                waiting_list.append((temp, index))
        return result 
